from sqlalchemy import Column, Integer, String
from database import db


class Business(db.Model):
    __tablename__ = 'business'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    points_to_offer = Column(Integer)

    def __init__(self, name, points_to_offer):
        self.name = name
        self.points_to_offer = points_to_offer

    def __repr__(self):
        return "<Business(name='%s')>" % self.name
