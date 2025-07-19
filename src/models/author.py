from src.ext import db
from src.models.base import BaseModel

class Author(BaseModel):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    poems = db.relationship('Poem', back_populates='author')