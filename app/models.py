from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


from app import app


db = SQLAlchemy(app)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    short_url = db.Column(db.String(6), unique = True, nullable = False)
    long_url = db.Column(db.String(255), nullable = False)
    date = db.Column(db.DateTime, default = datetime.now())
    count_view = db.Column(db.Integer, default = 0)


with app.app_context():
    db.create_all()