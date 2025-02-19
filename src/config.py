from os import path

class Config:
    BASE_DIR = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIR, "static")
    SECRET_KEY = "SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIR, "database.db")