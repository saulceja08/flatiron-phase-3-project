import click
from app.models import User, Workout, Session

@click.command()
@click.option('--user_id', prompt='Username', help='Username who will own this deletion')
@click.option('--workout_id', prompt='Workout ID', type=int, help='Workout ID you would like to delete')
def delete_workout(user_id, workout_id):
    session = Session()

    user = session.query(User).filter_by(username=user_id).first()

    if not user:
        return click.echo('User not found.')

    workout = session.query(Workout).filter_by(id=workout_id, user_id=user_id).first()

    if not workout:
        return click.echo('Workout not found for the user.')

    session.delete(workout)
    session.commit()

    click.echo('Workout deleted successfully!')

if __name__ == '__main__':
    delete_workout()