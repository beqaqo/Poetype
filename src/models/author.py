from src.ext import db
from src.models.base import BaseModel

class Author(db.Model, BaseModel):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    poem = db.relationship('Poem', back_populates='author')