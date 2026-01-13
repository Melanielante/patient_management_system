from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.services.consent_service import ConsentService
from app.models.healthcare_worker import HealthcareWorker

from app.db.session import get_db
from app.models.patient import Patient
from app.models.user import User
from app.middleware.dependency import require_role
from app.services.registry_service import RegistryService

router = APIRouter(prefix="/patients", tags=["patients"])


class PatientRegisterRequest(BaseModel):
    national_id: str


@router.get("/me")
def get_my_patient_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("patient"))
):
    patient = db.query(Patient).filter(
        Patient.user_id == current_user.id
    ).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient profile not found")

    return patient


@router.get("/{patient_id}")
def get_patient_by_id(
    patient_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("healthcare_worker"))
):
    worker = db.query(HealthcareWorker).filter(
        HealthcareWorker.user_id == current_user.id
    ).first()

    if not worker:
        raise HTTPException(status_code=403, detail="Worker profile not found")

    has_consent = ConsentService.has_valid_consent(
        db,
        patient_id=patient_id,
        facility_id=worker.facility_id,
        required_type="view"
    )

    if not has_consent:
        raise HTTPException(
            status_code=403,
            detail="No valid consent to access patient data"
        )

    patient = db.query(Patient).filter(
        Patient.patient_id == patient_id
    ).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


@router.post("/register")
def register_patient(
    data: PatientRegisterRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("patient"))
):
    registry_record = RegistryService.verify_patient(data.national_id)

    if not registry_record:
        raise HTTPException(
            status_code=400,
            detail="Patient not found in national registry"
        )

    existing = db.query(Patient).filter(
        Patient.user_id == current_user.id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Patient profile already exists"
        )

    patient = Patient(
        user_id=current_user.id,
        national_id_encrypted=f"mock_encrypted::{data.national_id}",
        first_name=registry_record["first_name"],
        last_name=registry_record["last_name"],
        date_of_birth=registry_record["date_of_birth"],
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient
