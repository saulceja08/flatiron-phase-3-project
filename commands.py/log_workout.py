import click
from app.models import Workout, sessionmaker

@click.command()
@click.option('--user_id', prompt=User ID, type=int, help='User ID who will own this workout')
@click.option('--duration_minutes', propmt='Duration(minutes)', type=int,help='Total minutes for workout')

def log_workout():
    session = Session()

    user = session.query(User).filter_by(member_id=user_id).first()

    if not user:
        return click.echo('User not found.')
    
    new_workout = Workout(
        duration_minutes=duration_minutes,
        user_id=user_id
    )

    session.add(new_workout)
    session.commit()

    click.echo('Workout was logged successfully!')

if __name__ == '__main__':
    log_workout()