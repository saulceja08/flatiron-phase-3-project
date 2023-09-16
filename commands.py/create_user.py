import click
from app.models import User

@click.command()
@click.option('--username', prompt='Username', help='Username to login')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='Password to login')
@click.option('--last_name', prompt='Last Name', help='Username last name')
@click.option('--birth_date', prompt='Birth Date (YYY-MM-DD)', type=click.DateTime(formats=["%Y-%m-%d"]), help='Username birthdate')
@click.option('--email', prompt='Email', help='Email address for the new user')
