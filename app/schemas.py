from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint
class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True  
    


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class res_user(BaseModel):
    id:int
    email: EmailStr
    created_at:datetime
    class Config:
        from_attributes = True
    
    
class UserLogin(BaseModel):
    email: EmailStr 
    password: str
    
    
    
class Token (BaseModel):
    access_token: str 
    token_type: str
class TokenData(BaseModel):
    id: Optional[int] = None


class responsE(PostCreate):
    id:int
    owner_id:int
    owner : res_user
    class Config:
        from_attributes = True

class Votes(BaseModel):
    post_id:int
    dir: conint(le=1)
    