from sqlalchemy import Column, Integer, Boolean, ForeignKey
from database import db


class Point(db.Model):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    business_id = Column(Integer, ForeignKey('business.id'))
    active_round = Column(Boolean, default=True, nullable=False)

    def __init__(self, user_id, business_id):
        self.user_id = user_id
        self.business_id = business_id

    def __repr__(self):
        return "<Point(id='%s')>" % self.id
