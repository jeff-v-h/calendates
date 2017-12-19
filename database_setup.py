import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendarevents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

event_dates = db.Table('event_dates',
	Column('date_id', Integer, ForeignKey('date.id')),
	Column('event_id', Integer, ForeignKey('event.id'))
)

class Date(db.Model):
	__tablename__ = 'date'
	id = Column(Integer, primary_key=True)
	year = Column(Integer) #?? nullable since some events may not know exact date yet 
	month = Column(Integer)
	month_name = Column(String(9))
	date = Column(Integer)
	day = Column(String(8))
	events = relationship('Event', secondary=event_dates, backref='dates')

	def __repr__(self):
		return '<User %r>' % self.id

class Event(db.Model):
	__tablename__ = 'event'
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	description = Column(String(1000))
	country = Column(String(50))
	city = Column(String(50))

	def __repr__(self):
		return '<Event %r>' % self.name

db.create_all()