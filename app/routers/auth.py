#ye hamlog sys,os se bhi krsakte ,the way we do in user.py and post.py,    but here we are doing ".." for going up the directory, means dono se kaam ho rha

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

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
import utilis

routers = APIRouter(tags=['Authentications'])

@routers.post("/login", response_model=schemas.Token)
def user_log(user_credential: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == user_credential.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    
    alpha = utilis.verify(user_credential.password, user.password)
    if not alpha:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    
    
    #create token here
    access_token = oauth.create_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}