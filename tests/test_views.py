import pytest
from src.models import Author, Poem


def test_index_page(client, app):
    with app.app_context():
        # Create test data
        author = Author(name="Test Author")
        author.save()
        
        poem = Poem(name="Test Poem", verse="This is a test poem", author=author)
        poem.save()
        
        # Test the index page
        response = client.get(f'/{author.id}/{poem.id}')
        assert response.status_code == 200
        assert b'Test Author' in response.data
        assert b'Test Poem' in response.data


def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200


def test_404_error(client):
    response = client.get('/nonexistent-page')
    assert response.status_code == 404 