from flask import Flask

from src.config import Config
from src.views import main_bp, errors_bp
from src.ext import db, migrate, admin
from src.commands import init_db, populate_db
from src.admin import init_admin

BLUEPRINTS = [main_bp, errors_bp]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
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
    init_admin(app, db)


def register_commands(app):
    for cmd in COMMANDS:
        app.cli.add_command(cmd)
