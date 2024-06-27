#!/usr/bin/python3
"""
This is the state class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
import models
import shlex

Base = declarative_base()

class State(BaseModel, Base):
    """
    This is the class for State.
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """
        Getter for cities related to the state.
        """
        all_cities = models.storage.all()
        state_cities = []

        for key, value in all_cities.items():
            if isinstance(value, City) and value.state_id == self.id:
                state_cities.append(value)

        return state_cities
