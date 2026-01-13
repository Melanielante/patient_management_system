from typing import Optional
from datetime import date

# Mock registry data (simulating government system)
MOCK_REGISTRY = {
    "12345678": {
        "first_name": "Melanie",
        "last_name": "Akinyi",
        "date_of_birth": date(1999, 5, 12),
    },
    "87654321": {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": date(1985, 8, 20),
    },
}

class RegistryService:
    @staticmethod
    def verify_patient(national_id: str) -> Optional[dict]:
        """
        Simulate verifying a patient against a national registry
        """
        return MOCK_REGISTRY.get(national_id)
