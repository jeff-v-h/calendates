from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Date, Event

engine = create_engine('sqlite:///calendarevents.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/calendates/', methods=['GET', 'POST'])
def homePage():
	# filter to first of January for each year so one object with each is obtained. then use the year column to list out all the years in the database.
	obj_with_each_year = session.query(Date).filter(Date.date == 1, Date.month == 1).all()
	return render_template('homepage.html', years = obj_with_each_year)

@app.route('/calendates/<int:year>/', methods=['GET', 'POST'])
def year(year):
	months = session.query(Date).filter_by(year = year, date = 1).all()
	return render_template('year.html', year = year, months = months)

@app.route('/calendates/<int:year>/<int:month>/', methods=['GET', 'POST'])
def month(year, month):
	monthobj = session.query(Date).filter_by(month = month).first()
	dates = session.query(Date).filter_by(year = year, month = month).all()
	return render_template('month.html', year=year, monthobj=monthobj, dates=dates)

@app.route('/calendates/<int:year>/<int:month>/<int:date>/', methods=['GET', 'POST'])
def date(year, month, date):
	date = session.query(Date).filter_by(year=year, month=month, date=date).one()
	return render_template('date.html', date = date)

@app.route('/calendates/events/', methods=['GET', 'POST'])
def events():
	return render_template('events.html')

@app.route('/calendates/newevent/', methods=['GET', 'POST'])
def newEvent():
	return render_template('newevent.html')

@app.route('/calendates/about/', methods=['GET', 'POST'])
def about():
	return render_template('about.html')

@app.route('/calendates/contact/', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

## For running website on localhost:5000 in debug mode (automatic refresh of webserver on file save)
if __name__ == '__main__':
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)