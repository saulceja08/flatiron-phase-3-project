from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Create SQLite db file 
engine = create_engine('sqlite:///database/fitness.db', echo=True)

#Create all tables from models
Base.metadata.create_all(bind=engine)

#Create a session 
Session = sessionmaker(bind=engine)
session = Session()
