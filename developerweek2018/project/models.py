# -*- coding: utf-8 -*-
"""Project models."""
import datetime as dt

from developerweek2018.database import Column, Model, SurrogatePK, db, reference_col, relationship
from developerweek2018.extensions import bcrypt


class Project(SurrogatePK, Model):
    """A project."""

    __tablename__ = 'projects'
    name = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Project({name})>'.format(name=self.name)
