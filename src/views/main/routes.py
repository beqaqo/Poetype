from flask import Blueprint, render_template, redirect, url_for
from os import path

from src.models.poem import Poem
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIR, 'templates', 'main')
main_bp = Blueprint('main', __name__, template_folder=TEMPLATES_FOLDER)

@main_bp.route('/')
def index():
    return render_template('index.html')
