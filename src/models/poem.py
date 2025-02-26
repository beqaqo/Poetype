from src.ext import db
from src.models.base import BaseModel

class Poem(db.Model, BaseModel):
    __tablename__ = 'poem'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    verse = db.Column(db.String)

    author_id = db.Column(db.ForeignKey('author.id'))
    author = db.relationship('Author', back_populates='poem')
