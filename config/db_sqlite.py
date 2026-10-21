# db_sqlite.py

import os
from flask_sqlalchemy import SQLAlchemy

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DATABASE = os.path.join(DATA_DIR, "todo.db")


def get_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE
    return SQLAlchemy(app)


class Todo:
    def __init__(self, db):
        self.db = db
        self.todo = type(
            "Todo",
            (db.Model,),
            {
                "id": db.Column(db.Integer, primary_key=True),
                "title": db.Column(db.String(80)),
                "complete": db.Column(db.Boolean),
            },
        )
