# coding: utf-8
from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.String(120))
    srole =db.Column(db.Integer, default=0)
    hash_pass = db.Column(db.String(200))

    def is_authenticated(self):
        return False

    def is_active(self):
        return False

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.name)
class DbConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    host = db.Column(db.String(200),)
    port = db.Column(db.Integer,default=3306)
    user = db.Column(db.String(100))
    password = db.Column(db.String(300))
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())
class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    dev = db.Column(db.String(64))
    audit = db.Column(db.String(64))
    srole = db.Column(db.Integer, default=0)
    sql_content = db.Column(db.Text)
    db_config = db.Column(db.String(64))
    backup = db.Column(db.Boolean, default=True)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    finish_time = db.Column(db.DateTime)
    man_review_time = db.Column(db.DateTime)
    auto_review = db.Column(db.Text)
    execute_result = db.Column(db.Text)





