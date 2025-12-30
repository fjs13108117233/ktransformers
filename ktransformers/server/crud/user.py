from sqlalchemy.orm import Session
from ktransformers.server.models.user import User
from ktransformers.server.schemas.user import UserCreate
from ktransformers.server.utils.auth import get_password_hash
import time


def get_user_by_username(db: Session, username: str):
    """Get a user by username"""
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    """Get a user by email"""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    """Create a new user"""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        created_at=int(time.time())
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    """Authenticate a user"""
    from ktransformers.server.utils.auth import verify_password
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
