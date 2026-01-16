from sqlalchemy import create_engine 
from .config import settings
from sqlalchemy.orm import declarative_base,sessionmaker   
#SQLALCHEMY_DATABASE_URL = 'postgresql://‹username>:<password>@<ip-address/hostname>/‹database_name›'
SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:{settings.password}@{settings.host}/fastapi_server'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)
Base = declarative_base()


def get_db() :
    db = sessionlocal()
    try:
        yield db
    finally:
        db. close()