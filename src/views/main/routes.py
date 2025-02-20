from flask import Blueprint, render_template, redirect, url_for
from os import path

from src.models.poem import Poem
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIR, 'templates', 'main')
main_bp = Blueprint('main', __name__, template_folder=TEMPLATES_FOLDER)

poem = """ჩემო კალამო, ჩემო კარგო, რად გვინდა ტაში?
        რასაც ვმსახურებთ, მას ერთგულად კვლავ ვემსახუროთ,
        ჩვენ წმინდა სიტყვა უშიშარად მოვფინოთ ხალხში
        ბოროტთ საკლავად, — მათ სულთ-ხდომის სეირს ვუყუროთ.

        თუ კაცმა ვერ სცნო ჩვენი გული, ხომ იცის ღმერთმა,
        რომ წმინდა არის განზრახვა და სურვილი ჩვენი:
        აგვიყოლია სიყრმიდანვე ჩვენ ქართვლის ბედმა
        და დაე გვძრახონ, — ჩვენ მის ძებნით დავლიოთ დღენი.

        ჩემზედ ამბობენ: „ის სიავეს ქართვლისას ამბობს,
        ჩვენს ცუდს არ მალავს, ეგ ხომ ცხადი სიძულვილია!”
        ბრიყვნი ამბობენ, კარგი გული კი მაშინვე სცნობს —
        ამ სიძულვილში რაოდენიც სიყვარულია!"""

def format_word(word):
    return "".join(f'<span class="letter">{char}</span>' for char in word)

poem = format_word(poem)

@main_bp.route('/')
def index():
    return render_template('index.html', poem=poem)
