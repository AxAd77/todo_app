# db_mysql.py

from flask_sqlalchemy import SQLAlchemy


def get_db(app):
    # Provide your own MySQL connection string
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://<db_user>:<db_pass>@<db_host>/<db_name>"
    )
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
