from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ktransformers.server.schemas.user import UserCreate, UserLogin, Token, User
from ktransformers.server.crud.user import create_user, get_user_by_username, authenticate_user
from ktransformers.server.utils.auth import create_access_token, verify_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ktransformers.server.utils.sql_utils import SQLUtil


router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    """Dependency to get database session"""
    sql_util = SQLUtil()
    with sql_util.get_db() as db:
        yield db


@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if username already exists
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Create new user
    return create_user(db=db, user=user)


@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """Login and get access token"""
    user = authenticate_user(db, user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
def get_current_user(username: str = Depends(verify_token), db: Session = Depends(get_db)):
    """Get current user information"""
    user = get_user_by_username(db, username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
