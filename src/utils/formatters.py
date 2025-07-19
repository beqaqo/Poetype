from src.models import Author, Poem


def format_list(model):
    """Format model objects for display in navigation lists"""
    author_id = None
    poem_id = None

    if isinstance(model, Author):
        author_id = model.id
        poems_obj = Poem.query.filter_by(author_id=model.id).all()
        if poems_obj:
            poem = poems_obj[0]
            poem_id = poem.id
    elif isinstance(model, Poem):
        poem_id = model.id
        author_id = model.author_id

    return f'<li class=""><a class="navbar-brand font-geo font-modal font-color-faded" href="/{author_id}/{poem_id}">{model.name}</a></li>'


def format_text(poem_text):
    """Format poem text for display with proper spacing"""
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