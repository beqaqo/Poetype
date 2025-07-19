import pytest
from src.models import Author, Poem


def test_author_creation(app):
    with app.app_context():
        author = Author(name="Test Author")
        author.save()
        
        assert author.id is not None
        assert author.name == "Test Author"


def test_poem_creation(app):
    with app.app_context():
        author = Author(name="Test Author")
        author.save()
        
        poem = Poem(name="Test Poem", verse="This is a test poem", author=author)
        poem.save()
        
        assert poem.id is not None
        assert poem.name == "Test Poem"
        assert poem.author_id == author.id


def test_author_poem_relationship(app):
    with app.app_context():
        author = Author(name="Test Author")
        author.save()
        
        poem1 = Poem(name="Poem 1", verse="First poem", author=author)
        poem2 = Poem(name="Poem 2", verse="Second poem", author=author)
        poem1.save()
        poem2.save()
        
        assert len(author.poems) == 2
        assert poem1 in author.poems
        assert poem2 in author.poems 