import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    # 3 columns SQLAlchemy must match instance properties(self.id, username, password)
    # instance object/property - SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)  # auto incremental
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod  # create a special class instance
    # search input username at the sql database
    def find_by_username(cls, username):
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # select_query = "SELECT* FROM users WHERE username=?"
        # result = cursor.execute(select_query, (username, ))
        # row = result.fetchone()
        # if row:
        #     user = cls(row[0], row[1], row[2])
        # else:
        #     user = None
        #
        # connection.close()

        return cls.query.filter_by(username=username).first()

    @classmethod  # create a special class instance
    # search input username at the sql database
    def find_by_userid(cls, _id):

        return cls.query.filter_by(id=_id).first()