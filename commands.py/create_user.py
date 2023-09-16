import click
from app.models import User
from main import Session 

@click.command()
@click.option('--username', prompt='Username', help='Username to login')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='Password to login')
@click.option('--last_name', prompt='Last Name', help='Username last name')
@click.option('--birth_date', prompt='Birth Date (YYY-MM-DD)', type=click.DateTime(formats=["%Y-%m-%d"]), help='Username birthdate')
@click.option('--email', prompt='Email', help='Email address for the new user')

def create_user(username, password, first_name, last_name, birth_date, email):
    session = Session()

    new_user = User(
        username = username,
        password = password,
        first_name = first_name,
        last_name = last_name,
        birth_date = birth_date,
        email = email
    )

    session.add(new_user)
    session.commi()

    click.echo('User successfully created!')

if __name__ == "__main__":
    create_user()