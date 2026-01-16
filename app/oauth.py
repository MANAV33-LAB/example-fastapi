from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import HTTPException,Depends,status
import schemas,database,model
from sqlalchemy.orm import Session
# 3 things to provide -> SECRET_KEY,ALGORITHM,EXPIRATION_TIME
from fastapi.security import OAuth2PasswordBearer #use for automatic extract token from request in get_curr_user and then pass to verify to check
SECRET_KEY ="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"#ARBITARY LONG TEXT
ALGORITHM = "HS256"
TOKEN_EXPIRE_TIME = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data:dict):
    data2 = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_TIME)
    data2.update({"exp":expire}) #syntax "exp" rahega
    encoded_jwt = jwt.encode(data2,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        
        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)
        return token_data
        
    except JWTError:
        raise credentials_exception
    return token_data
def get_current_user(token: str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    alpha = verify_access_token(token, credentials_exception)
    beta = db.query(model.User).filter(model.User.id == alpha.id).first()
    return beta
    
