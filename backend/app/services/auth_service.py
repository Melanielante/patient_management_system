from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password

def create_user(db: Session, email: str, password: str, role: str):
    user = User(
        email=email,
        password_hash=hash_password(password),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
