import click
from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from commands.create_user import create_user
from commands.log_workout import log_workout
from commands.log_weight import log_weight
from commands.delete_workout import delete_workout

#Create SQLite db file 
engine = create_engine('sqlite:///database/fitness.db', echo=True)

#Create all tables from models
Base.metadata.create_all(bind=engine)

#Create a session 
Session = sessionmaker(bind=engine)
session = Session()


@click.command()
def cli():
    print('Hello User! What would you like to do today?')

    commands = ['create_user', 'log_workout', 'log_weight', 'delete_workout']

    selected_command = click.prompt('Choose a command:', type=click.Choice(commands))
    if selected_command == 'create_user':
        create_user()
    elif selected_command == 'log_workout':
        log_workout()
    elif selected_command == 'log_weight':
        log_weight()
    elif selected_command == 'delete_workout':
        delete_workout()

if __name__== '__main__':
    cli()