from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database_setup import db, Date, Event, events_dates

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendarevents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
@app.route('/calendates/', methods=['GET', 'POST'])
def homePage():
	# filter to first of January for each year so one object with each is obtained. then use the year column to list out all the years in the database.
	obj_with_each_year = Date.query.filter(Date.date == 1, Date.month == 1).all()
	return render_template('homepage.html', years = obj_with_each_year)

@app.route('/calendates/<int:year>/', methods=['GET', 'POST'])
def year(year):
	months = Date.query.filter_by(year = year, date = 1).all()
	return render_template('year.html', year = year, months = months)

@app.route('/calendates/<int:year>/<int:month>/', methods=['GET', 'POST'])
def month(year, month):
	monthobj = Date.query.filter_by(month = month).first()
	dates = Date.query.join(Event.dates).filter_by(year=year, month=month).all()
	return render_template('month.html', year=year, monthobj=monthobj, dates=dates)

@app.route('/calendates/<int:year>/<int:month>/<int:date>/', methods=['GET', 'POST'])
def date(year, month, date):
	date = Date.query.filter_by(year=year, month=month, date=date).one()
	events = Event.query.filter(Event.dates.contains(date)).all()
	return render_template('date.html', date=date, events=events)

@app.route('/calendates/events/', methods=['GET', 'POST'])
def events():
	events = Event.query.all()
	return render_template('events.html', events=events)

@app.route('/calendates/newevent/', methods=['GET', 'POST'])
def newEvent():
	if request.method == 'POST':
		date = Date.query.filter_by(year=request.form['year'], month_name=request.form['month-name'], date=request.form['date']).one()
		if date:
			event = Event(name=request.form['name'], date_id=date.id, description=request.form['description'], country=request.form['country'], city=request.form['city'])
			db.session.add(event)
			db.session.commit()
			print event
			return redirect(url_for('date', year=date.year, month=date.month, date=date.date))
		else:
			print "date not found, try a proper date"
	else:
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

