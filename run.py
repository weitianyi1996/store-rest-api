from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()  # no longer need create_tables.py(using SQL to create table)