# Try relative imports first (for Render), fallback to absolute (for local)
try:
    from .. import model
    from .. import utilis
    from ..schemas import UserCreate, res_user
    from ..database import get_db
except ImportError:
    import model
    import utilis
    from schemas import UserCreate, res_user
    from database import get_db

from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

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