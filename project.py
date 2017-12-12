from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Date, Event
from datetime import date

engine = create_engine('sqlite:///calendarevents.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#temporary data
tempdate = {'year': 2018, 'id': 1, 'month': 2, 'month_name': 'February', 'date': 2, 'day': 'Monday'}

@app.route('/')
@app.route('/calendates/')
def homePage():
	return render_template('homepage.html')

@app.route('/calendates/<int:date_year>/')
def year(date_year):
	return render_template('year.html', date = tempdate)

@app.route('/calendates/<int:date_year>/<int:date_month>/')
def month(date_year, date_month):
	return render_template('month.html', date = tempdate)

@app.route('/calendates/<int:date_year>/<int:date_month>/<int:date_date>')
def date(date_year, date_month, date_date):
	return render_template('date.html', date = tempdate)

## For running website on localhost:5000 in debug mode (automatic refresh of webserver on file save)
if __name__ == '__main__':
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)