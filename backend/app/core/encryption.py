from cryptography.fernet import Fernet
import os

# Load from env 
FERNET_KEY = os.getenv("FERNET_KEY")

if not FERNET_KEY:
    raise RuntimeError("FERNET_KEY not set")

fernet = Fernet(FERNET_KEY.encode())


def encrypt_value(value: str) -> str:
    return fernet.encrypt(value.encode()).decode()


def decrypt_value(value: str) -> str:
    return fernet.decrypt(value.encode()).decode()
