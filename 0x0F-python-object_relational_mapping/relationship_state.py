#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
"""
    Module that performs creates a States class based off of Base.
"""
meta_data = MetaData()
Base = declarative_base(metadata = meta_data)


class State(Base):
    """
        The ``States`` class which inherits from ``Base`` class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref="state", cascade="all",
        single_parent=True)
