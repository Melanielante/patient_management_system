from sqlalchemy.orm import Session
from app.models.access_log import AccessLog


class AccessLogService:

    @staticmethod
    def log(
        db: Session,
        *,
        patient_id: str,
        accessed_by: str,
        facility_id: str,
        action: str,
        result: str,
        reason: str = None,
        ip_address: str = None
    ):
        log = AccessLog(
            patient_id=patient_id,
            accessed_by=accessed_by,
            facility_id=facility_id,
            action=action,
            result=result,
            reason=reason,
            ip_address=ip_address,
        )

        db.add(log)
        db.commit()
