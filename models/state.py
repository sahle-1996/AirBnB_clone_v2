#!/usr/bin/python3
"""Defines the State class with storage and relationship handling"""

import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a state in the database
    Attributes:
        name: The name of the state
        cities: Relationship with cities in the state
    """

    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')

    else:
        name = ""

        @property
        def cities(self):
            """Gets list of City instances related to this State"""
            return [city for city in models.storage.all(models.City).values()
                    if city.state_id == self.id]
