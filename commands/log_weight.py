import click
from app.models import User, WeightTracker, Session

@click.command()
@click.option('--user_id',prompt='User ID',type=int, help='User ID who will own this weight')
@click.option('--current_weight',prompt='Current Weight(kg)',type=int, help='Weight after workout in kg')
@click.option('--previous_weight',prompt='Previous Weight(kg)',type=int, help='Weight before workout in kg')

def log_weight(user_id, current_weight, previous_weight):
    session = Session()

    user = session.query(User).filter_by(member_id=user_id).first()

    if not user:
        return click.echo('User not found.')
    
    new_weight_calc = WeightTracker(
        user_id=user_id,
        current_weight=current_weight,
        previous_weight=previous_weight
    )

    session.add(new_weight_calc)
    session.commit()

    click.echo('Weight has been logged successfully!')

if __name__=="__main__":
    session = Session()
    log_weight()
