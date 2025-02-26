from flask import Blueprint, render_template, redirect
from os import path


from src.models import Poem, Author
from src.config import Config

# Define templates folder path
TEMPLATES_FOLDER = path.join(Config.BASE_DIR, 'templates', 'main')
main_bp = Blueprint('main', __name__, template_folder=TEMPLATES_FOLDER)


# Utility functions
def format_list(author):
    author_id = None
    poem_id = None

    if type(author) == Author:
        author_id = author.id
        poems_obj = Poem.query.filter_by(author_id=author.id).all()
        poem = poems_obj[0]
        poem_id = poem.id
    if type(author) == Poem:
        poem_id = author.id
        author_id = author.author_id

    return f'<li class=""><a class="navbar-brand font-geo font-m font-color" href="/{author_id}/{poem_id}">{author.name}</a></li>'

def format_text(poem_text):
    return ''.join(f'<span class="letter">{char}</span>' for char in poem_text)

# Routes
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