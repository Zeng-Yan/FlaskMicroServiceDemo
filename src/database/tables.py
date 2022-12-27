# cython: language_level=3

from datetime import datetime

from src.database.exts import db, EnhancedTable


class Point(EnhancedTable, db.Model):
    __tablename__ = 'point'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)


class Target(EnhancedTable, db.Model):
    __tablename__ = 'target'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    identifier = db.Column(db.Integer)
    time = db.Column(db.DateTime, default=datetime.utcnow())
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    # 22-25, 120-122
