from app.models import Base
from sqlalchemy import create_engine

#Create SQLite db file 
engine = create_engine('sqlite:///db/fitness.db')

#Create the tables from models
Base.metadata.create_all(engine)

