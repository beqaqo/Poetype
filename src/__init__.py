from flask import Flask
from flask_admin.contrib.sqla import ModelView

from src.config import Config
from src.views import main_bp
from src.ext import db, migrate, admin
from src.commands import init_db, populate_db
from src.models import Author, Poem

BLUEPRINTS = [main_bp]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)

    register_blueprints(app)

    register_commands(app)

    return app


def register_blueprints(app):
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    # admin.init_app(app)
    #
    # class PoemAdmin(ModelView):
    #     form_columns = ['name', 'verse', 'author']  # Include author field
    #     form_ajax_refs = {
    #         'author': {
    #             'fields': ['name']  # Search authors by name
    #         }
    #     }
    # class AuthorAdmin(ModelView):
    #     form_columns = ['name']
    #
    # admin.add_view(PoemAdmin(Poem, db.session))
    # admin.add_view(AuthorAdmin(Author, db.session))


def register_commands(app):
    for cmd in COMMANDS:
        app.cli.add_command(cmd)
