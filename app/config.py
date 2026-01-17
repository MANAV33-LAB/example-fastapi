from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # Database
    host: str
    port: str
    password: str
    database: str
    user: str
    
    # JWT
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

# Create instance
settings = Settings()