from src.ext import db
from src.models.base import BaseModel

class Poem(BaseModel):
    __tablename__ = 'poem'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    verse = db.Column(db.Text)
    author_id = db.Column(db.ForeignKey('author.id'))

    author = db.relationship('Author', back_populates='poems')