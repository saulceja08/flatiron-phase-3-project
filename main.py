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
    
    def __init__(self, member_id, username, first_name, last_name, birth_date, email):
        self.member_id = member_id\
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email

    def __repr__(self):
        return f"{self.member_id}{self.username}{self.first_name}{self.last_name}{self.birth_date}{self.email}"
    

#connection to a database so that we can interact with it (echo logs SQL statements into console)
engine = create_engine("sqllite:///fitness.db", echo=True)
base.metadata.create_all(bind=engine)

#create a session class and object to interact using ORM
Session = sessionmaker(bind=engine)
session = Session()