from app.models import Base
from sqlalchemy import create_engine

#Create SQLite db file 
engine = create_engine('sqlite:///db/fitness.db', echo=True)

#Create all tables from models
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()
