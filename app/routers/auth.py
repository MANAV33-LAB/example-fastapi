#ye hamlog sys,os se bhi krsakte ,the way we do in user.py and post.py,    but here we are doing ".." for going up the directory, means dono se kaam ho rha

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

# Try relative imports first (for Render), fallback to absolute (for local)
try:
    from .. import model
    from .. import schemas
    from .. import utilis
    from .. import oauth
    from ..database import get_db
except ImportError:
    import model
    import schemas
    import utilis
    import oauth
    from database import get_db

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