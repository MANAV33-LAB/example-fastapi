import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
import database,schemas,model,utilis,oauth #hamlog sys,os se bhi krsakte ,the way we do in user.py and post.py,    but here we are doing ".." for going up the directory, means dono se kaam ho rha

routers = APIRouter(tags = ['Authentications'])

@routers.post("/login",response_model=schemas.Token)
def user_log(user_credential:schemas.UserLogin,db:Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email == user_credential.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    
    alpha = utilis.verify(user_credential.password,user.password)
    if not alpha:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    
    
    #create token here
    access_token = oauth.create_token(data = {"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}
        
    
