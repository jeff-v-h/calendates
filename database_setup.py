import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Date(Base):
	__tablename__ = 'date'
	id = Column(Integer, primary_key=True)
	year = Column(Integer) #?? nullable since some events may not know exact date yet 
	month = Column(Integer)
	month_name = Column(String(9))
	date = Column(Integer)
	day = Column(String(8))
	events = relationship('Event', backref='date', lazy=True)

class Event(Base):
	__tablename__ = 'month'
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	date_id = Column(Integer, ForeignKey('date.id'), nullable=False)


engine = create_engine('sqlite:///calendarevents.db')
Base.metadata.create_all(engine)