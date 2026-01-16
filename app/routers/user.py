import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import model
from schemas import UserCreate,res_user
import utilis

from fastapi import  status, HTTPException, Depends,APIRouter

from sqlalchemy.orm import Session
from database import get_db
routers = APIRouter(
    tags=["USERS"]
)

@routers.post("/users", response_model=res_user)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists BEFORE trying to insert
    existing_user = db.query(model.User).filter(
        model.User.email == user.email
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    
    
    passw = utilis.hashi(user.password)
    user.password = passw
    
    
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user



