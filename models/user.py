from sqlalchemy import Column, Integer, String
from database import db


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<User(email='%s')>" % self.email
