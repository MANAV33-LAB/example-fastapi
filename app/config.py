from pydantic_settings import BaseSettings
import os

class setting(BaseSettings):
    password:str
    host:str
    class Config:
        env_file = env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        
#yahan aur bhi password or things add krsakte,but as this is for practice i do oinly two,but we should add multiplt for safety purpose
    
settings = setting()
        