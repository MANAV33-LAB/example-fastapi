from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import Relationship

from sqlalchemy.sql.expression import text
# Use try-except for both cases
try:
    # For normal running (from app folder)
    from database import Base
except ImportError:
    # For Alembic (from root folder)
    from .database import Base

class Post(Base):
    __tablename__ = "posts"#column name
    
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("USERS.id",ondelete = "CASCADE"),nullable=False)
    owner = Relationship("User")#bas ek schema mein aur add kro ,bas ye automatically user ka infor sath sath dega ,better then owner id


class User(Base):
    __tablename__ = "USERS"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable =False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class votes(Base):
    __tablename__= "VOTES"
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True,nullable=False)
    user_id = Column(Integer,ForeignKey("USERS.id",ondelete="CASCADE"),primary_key=True,nullable=False)
