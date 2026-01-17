from sqlalchemy import create_engine 
# Add try-except for config too
try:
    from config import settings
except ImportError:
    from .config import settings
from sqlalchemy.orm import declarative_base,sessionmaker   
#SQLALCHEMY_DATABASE_URL = 'postgresql://‹username>:<password>@<ip-address/hostname>/‹database_name›'
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)
Base = declarative_base()


def get_db() :
    db = sessionlocal()
    try:
        yield db
    finally:
        db. close()