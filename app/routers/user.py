# Try relative imports first (for Render), fallback to absolute (for local)
# These files are in app/routers/
# Need to import from parent directory (app/)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import model        # This works because we added parent to path
import oauth
import schemas
from database import get_db
from schemas import UserCreate, res_user
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import utilis
routers = APIRouter(tags=["USERS"])

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