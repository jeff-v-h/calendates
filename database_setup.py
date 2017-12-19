import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendarevents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

events_dates = db.Table('events_dates',
	db.Column('date_id', db.Integer, db.ForeignKey('date.id'), primary_key=True),
	db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

class Date(db.Model):
	__tablename__ = 'date'
	id = db.Column(db.Integer, primary_key=True)
	year = db.Column(db.Integer) #?? nullable since some events may not know exact date yet 
	month = db.Column(db.Integer)
	month_name = db.Column(db.String(9))
	date = db.Column(db.Integer)
	day = db.Column(db.String(8))
	events = db.relationship('Event', secondary=events_dates, lazy='subquery', backref=db.backref('dates'))

	def __repr__(self):
		return '<Date %r, %r, %r>' % (self.year, self.month_name, self.date)

class Event(db.Model):
	__tablename__ = 'event'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(1000))
	country = db.Column(db.String(50))
	city = db.Column(db.String(50))

	def __repr__(self):
		return '<Event %r>' % self.name

db.create_all()