import click
from commands import create_user, log_workout, log_weight, delete_workout
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


@click.group
def cli():
    pass

    cli.add_command(create_user(session))
    cli.add_command(log_workout(session))
    cli.add_command(log_weight(session))
    cli.add_command(delete_workout(session))

if __name__== '__main__':
    cli()