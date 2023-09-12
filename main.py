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
    username = Column(String(25), unique=True, nullable=False)
    first_name = Column(String(25), unique=False, nullable=False)
    last_name = Column(String(25), unique=False, nullable=False)
    birth_date = Column(DateTime())
    email = Column(String(55), unique=True,nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)
    
    def __init__(self, username, first_name, last_name, birth_date, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
        self.email = email

    def __repr__(self):
        return f"<User({self.member_id}, {self.username}, {self.first_name}, {self.last_name}, {self.birth_date}, {self.email})>"

#connection to a database so that we can interact with it (echo logs SQL statements into console)
engine = create_engine("sqlite:///fitness.db", echo=True)
Base.metadata.create_all(bind=engine)

#create a session class and object to interact using ORM
Session = sessionmaker(bind=engine)
session = Session()

new_user = User("saulceja08", "Saul", "Ceja", "17-01-1999", "saulceja08@gmail.com")
session.add(new_user)
session.commit() #Note: This will commit the changes to the database 