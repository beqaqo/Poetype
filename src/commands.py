from flask.cli import with_appcontext
import click

from src.ext import db
from src.models import Poem, Author

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database")
    db.drop_all()
    db.create_all()
    click.echo("Initialized database")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database")