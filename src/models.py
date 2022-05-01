from email.policy import default
from operator import index
from platform import platform
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from src.database import Base
from sqlalchemy.orm import relationship


class Client(Base):
    # name
    __tablename__ = "clients" 
    # fields
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String)
    session_id = Column(String)
    sdk_version = Column(String)
    platform = Column(String)
    country_code = Column(Integer)
    # stats
    impressions = Column(Integer, default=0)   
    ads = Column(Integer,default=0)  
    
