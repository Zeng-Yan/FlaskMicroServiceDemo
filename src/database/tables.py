# cython: language_level=3

from datetime import datetime
from typing import Any, Dict

from src.database.exts import db, EnhancedTable


class Point(EnhancedTable, db.Model):
    __tablename__ = 'point'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class Target(EnhancedTable, db.Model):
    __tablename__ = 'target'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    identifier = db.Column(db.Integer)
    time = db.Column(db.DateTime, default=datetime.utcnow())
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)

    def __init__(self, **kwargs) -> None:
        for k in ('time', ):
            kwargs[k] = self.str_to_date(kwargs[k])
        super().__init__(**kwargs)
    
    def serialize(self) -> Dict[str, Any]:
        affine = super().serialize()
        for k in ('time', ):
            affine[k] = affine[k].strftime('%Y-%m-%d %H:%M:%S')
        return affine
