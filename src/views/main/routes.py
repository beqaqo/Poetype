from flask import Blueprint, render_template, redirect
from os import path

from src.models import Poem, Author
from src.config import Config

# Define templates folder path
TEMPLATES_FOLDER = path.join(Config.BASE_DIR, 'templates', 'main')
main_bp = Blueprint('main', __name__, template_folder=TEMPLATES_FOLDER)


# Utility functions
def format_list(model):
    author_id = None
    poem_id = None

    if type(model) == Author:
        author_id = model.id
        poems_obj = Poem.query.filter_by(author_id=model.id).all()
        poem = poems_obj[0]
        poem_id = poem.id
    if type(model) == Poem:
        poem_id = model.id
        author_id = model.author_id

    return f'<li class=""><a class="navbar-brand font-geo font-modal font-color-faded" href="/{author_id}/{poem_id}">{model.name}</a></li>'


def format_text(poem_text):
    poem_text = poem_text.replace("\n", "")
    text = ''
    prev_space = False  # Tracks if the last character was a space

    for char in poem_text:
        if char == ' ':
            prev_space = True  # Mark that we encountered a space
            text += f'<span class="letter">{char}</span>'  # Keep the first space
        elif prev_space and char == ' ':
            prev_space = False  # Reset when a non-space character appears
        else:
            text += f'<span class="letter">{char}</span>'

    return text


# Routes
@main_bp.route('/')
def this():
    return index(1, 1)


@main_bp.route('/<int:author_id>/<int:poem_id>', methods=['GET'])
def index(author_id, poem_id):
    author_obj = Author.query.get(author_id)
    poems_obj = Poem.query.filter_by(author_id=author_id).all()
    poem_obj = Poem.query.get(poem_id)

    authors = "".join(format_list(author) for author in Author.query.all())
    poems = "".join(format_list(poem) for poem in poems_obj)
    formatted_poem = format_text(poem_obj.verse)
    word_count = len(poem_obj.verse.split())

    return render_template(
        'index.html',
        author=author_obj.name,
        authors=authors,
        poem_name=poem_obj.name,
        poems=poems,
        poem=formatted_poem,
        count=word_count
    )


@main_bp.route('/about')
def about():
    return render_template('about.html')
