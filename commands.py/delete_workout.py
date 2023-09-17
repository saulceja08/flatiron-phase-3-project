import click
from app.models import Workout, sessionmaker

@click.command()
@click.option('--user_id', prompt='User ID', type=int, help='User ID who will own this deletion')
@click.option('--workout_id',prompt='Workout ID',type=int,help='Worokout ID you would like to delete')

def delete_workout(user_id, workout_id):
    pass

