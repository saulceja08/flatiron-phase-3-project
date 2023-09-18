import click
from app.models import User, Workout, Session

@click.command()
@click.prompt('--user_id', prompt='User ID', type=int, help='User ID who will own this deletion')
@click.prompt('--workout_id',prompt='Workout ID',type=int,help='Worokout ID you would like to delete')

def delete_workout(user_id, workout_id):
    session = Session()

    user = session.query(User).filter_by(member_id=user.id).first()

    if not user:
        return click.echo('User not found.')
    
    workout = session.query(Workout).filter_by(id=workout_id, user_id=user_id).first()

    if not workout:
        return click.echo('Workout not found for the user.')
    
    session.delete(workout)
    session.commit()

    click.echo('Workout deleted successfully!')

if __name__=='__main__':
    delete_workout()