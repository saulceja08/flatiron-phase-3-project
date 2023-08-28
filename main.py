from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

#define the base class 
Base = declarative_base() 

#Define the User class that will inherti from the base class -saulceja
class User(Base):
    __tablename__ = "users"

    member_id = Column(Integer, primary_key=True, unique=True)
    usernname = Column(String(25), unique=True, nullable=False)
    first_name = Column(String(25), unique=False, nullable=False)
    last_name = Column(String(25), unique=False, nullable=False)
    birth_date = Column(DateTime())
    email = Column(String(25), unique=True,nullable=False)

