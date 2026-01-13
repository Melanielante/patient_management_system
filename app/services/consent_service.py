from sqlalchemy.orm import Session
from datetime import datetime
from app.models.consent import Consent


class ConsentService:

    @staticmethod
    def has_valid_consent(
        db: Session,
        *,
        patient_id: str,
        facility_id: str,
        required_type: str
    ) -> bool:
        """
        Check if a facility has active, non-expired consent
        with required permission level.
        """

        now = datetime.utcnow()

        consent = (
            db.query(Consent)
            .filter(
                Consent.patient_id == patient_id,
                Consent.facility_id == facility_id,
                Consent.status == "active",
                Consent.revoked_at.is_(None),
            )
            .order_by(Consent.granted_at.desc())
            .first()
        )

        if not consent:
            return False

        if consent.expires_at and consent.expires_at < now:
            return False

        # Permission hierarchy
        allowed = {
            "view": ["view", "edit", "share"],
            "edit": ["edit", "share"],
            "share": ["share"],
        }

        return required_type in allowed.get(consent.consent_type, [])
