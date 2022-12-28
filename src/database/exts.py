# cython: language_level=3

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from typing import Any, Dict

db = SQLAlchemy()


class EnhancedTable:
    """
    offering some universal functions and attributes to enhance Table of db.Model.
    """
    __table_args__ = {'extend_existing': True}

    def __getitem__(self, key):
        """
        make object indexable.
        """
        return self.__dict__.get(key)

    def serialize(self) -> Dict[str, Any]:
        """
        serialize a record into dict-format like {'key': value}.
        """
        affine = {key: value for key, value in self.__dict__.items()
                  if key != '_sa_instance_state'}
        return affine
