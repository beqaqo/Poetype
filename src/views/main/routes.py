from flask import Blueprint, render_template, redirect

from src.models import Poem, Author
from src.utils.formatters import format_list, format_text

main_bp = Blueprint('main', __name__)


# Routes
@main_bp.route('/')
def this():
    return index(1, 1)


@main_bp.route('/<int:author_id>/<int:poem_id>', methods=['GET'])
def index(author_id, poem_id):
    author_obj = Author.query.get(author_id)
    poems_obj = Poem.query.filter_by(author_id=author_id).all()
    poem_obj = Poem.query.get(poem_id)

    if not author_obj or not poem_obj:
        return "Author or poem not found", 404
    if int(poem_obj.author_id) != int(author_id):
        return index(1, 1)

    authors = "".join(format_list(author) for author in sorted(Author.query.all(), key=lambda x: x.name))
    poems = "".join(format_list(poem) for poem in sorted(poems_obj, key=lambda x: x.name))

    formatted_poem = format_text(poem_obj.verse)
    word_count = len(poem_obj.verse.split())

    return render_template(
        'main/index.html',
        author=author_obj.name,
        authors=authors,
        poem_name=poem_obj.name,
        poems=poems,
        poem=formatted_poem,
        count=word_count
    )


@main_bp.route('/about')
def about():
    return render_template('main/about.html')
