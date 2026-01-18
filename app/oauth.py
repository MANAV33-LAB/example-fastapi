from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, status
import schemas, database, model
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials  # CHANGED LINE
try:
    from .config import settings
except ImportError:
    from config import settings

# Use environment variables from settings
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# CHANGED: Using HTTPBearer instead of OAuth2PasswordBearer
oauth2_scheme = HTTPBearer()

def create_token(data: dict):
    data2 = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data2.update({"exp": expire})
    encoded_jwt = jwt.encode(data2, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        
        if id is None:
            raise credentials_exception  # Only raises if user_id is missing
        
        token_data = schemas.TokenData(id=id)
        return token_data
        
    except JWTError:
        raise credentials_exception  # Only raises if JWT is invalid

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    # Create error message template (not thrown yet)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    # Extract token from credentials object
    token = credentials.credentials
    
    # Verify token - this function WILL throw error ONLY if token is invalid
    alpha = verify_access_token(token, credentials_exception)
    
    # Get user from database
    beta = db.query(model.User).filter(model.User.id == alpha.id).first()
    
    return beta