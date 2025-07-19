from flask_admin.contrib.sqla import ModelView
from src.ext import admin
from src.models import Poem, Author


class PoemAdmin(ModelView):
    form_columns = ['name', 'verse', 'author']
    form_ajax_refs = {
        'author': {'fields': ['name']}
    }


class AuthorAdmin(ModelView):
    form_columns = ['name']


def init_admin(app, db):
    admin.init_app(app)
    admin.add_view(PoemAdmin(Poem, db.session))
    admin.add_view(AuthorAdmin(Author, db.session)) 