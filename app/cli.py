import click

@click.group()
def cli():
    pass 

@cli.command()
def create_user():
    pass

@cli.command()
def log_workout():
    pass

@cli.command()
def log_weight():
    pass

@cli.command()
def delete_workout():
    pass

if __name__ =="__main__":
    cli()