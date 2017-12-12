import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

date_event_association = Table('association', Base.metadata, 
	Column('date_id', Integer, ForeignKey('date.id')),
	Column('event_id', Integer, ForeignKey('event.id'))
)

class Date(Base):
	__tablename__ = 'date'
	id = Column(Integer, primary_key=True)
	year = Column(Integer) #?? nullable since some events may not know exact date yet 
	month = Column(Integer)
	month_name = Column(String(9))
	date = Column(Integer)
	day = Column(String(8))
	events = relationship('Event', secondary=date_event_association, backref='dates')

class Event(Base):
	__tablename__ = 'month'
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	