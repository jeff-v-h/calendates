import os
from settings import app, db
from flask import Flask, render_template, request, redirect, url_for
from database_setup import Date, Event, events_dates

@app.route('/')
@app.route('/calendates/', methods=['GET', 'POST'])
def homePage():
	# filter to first of January for each year so one object with each is obtained. then use the year column to list out all the years in the database.
	obj_with_each_year = Date.query.filter(Date.date == 1, Date.month == 1).all()
	return render_template('homepage.html', years = obj_with_each_year)

@app.route('/calendates/about/', methods=['GET', 'POST'])
def about():
	return render_template('about.html')

@app.route('/calendates/contact/', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

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
	events = Event.query.join(Date.events).order_by(Date.year.asc()).order_by(Date.month.asc()).order_by(Date.date.asc()).all()
	return render_template('events.html', events=events)

@app.route('/calendates/newevent/', methods=['GET', 'POST'])
def newEvent():
	if request.method == 'POST':
		if request.form['name']:
			year = int(request.form['year'])
			month = int(request.form['month'])
			date = int(request.form['date'])
			dateStart = Date.query.filter_by(year=year, month=month, date=date).one()
			newDates = []
			event = Event(name=request.form['name'], description=request.form['description'], country=request.form['country'], city=request.form['city'])
			if dateStart:
				if request.form.get('multiple-days'): #change multiple dates
					yearEnd = int(request.form['year-end'])
					monthEnd = int(request.form['month-end'])
					dateEnd = int(request.form['date-end'])
					dateIsAfter = checkDates(year, month, date, yearEnd, monthEnd, dateEnd)
					if dateIsAfter:
						allSame = False
						while not allSame:
							newDate = Date.query.filter_by(year=year, month=month, date=date).one()
							newDates.append(newDate)
							if (year==yearEnd and month==monthEnd and date==dateEnd):
								allSame = True
							else:
								year, month, date = getNextDate(year, month, date)
						event.dates = [] #needed to get rid of all dates, otherwise if overlap will cause dates not to be in order.
						event.dates = newDates
					else:
						print "You need to make sure the 2nd date is after the first"
				else: #just change 1 date
					print "multiple days not ticked"
					newDates.append(dateStart)
					event.dates = newDates
			else:
				print "date not found, try a proper date. date not changed"
				return
			db.session.add(event)
			db.session.commit()
			return redirect(url_for('events'))
		else:
			print "Event must have a name"
			return	
	else:
		return render_template('newevent.html')

@app.route('/calendates/events/<int:event_id>/', methods=['GET', 'POST'])
def eventInfo(event_id):
	event = Event.query.filter_by(id=event_id).one()
	if request.method == 'POST':
		if request.form['name']:
			event.name = request.form['name']
			event.description = request.form['description']
			event.country = request.form['country']
			event.city = request.form['city']
			year = int(request.form['year'])
			month = int(request.form['month'])
			date = int(request.form['date'])
			dateStart = Date.query.filter_by(year=year, month=month, date=date).one()
			newDates = []
			if dateStart: #make sure date is in database
				if request.form.get('multiple-days'): #change multiple dates
					yearEnd = int(request.form['year-end'])
					monthEnd = int(request.form['month-end'])
					dateEnd = int(request.form['date-end'])
					dateIsAfter = checkDates(year, month, date, yearEnd, monthEnd, dateEnd)
					if dateIsAfter:
						allSame = False
						while not allSame:
							newDate = Date.query.filter_by(year=year, month=month, date=date).one()
							newDates.append(newDate)
							if (year==yearEnd and month==monthEnd and date==dateEnd):
								allSame = True
							else:
								year, month, date = getNextDate(year, month, date)
						event.dates = [] #needed to get rid of all dates, otherwise if overlap will cause dates not to be in order.
						event.dates = newDates
					else:
						print "You need to make sure the 2nd date is after the first"
				else: #just change 1 date
					print "multiple days not ticked"
					newDates.append(dateStart)
					event.dates = newDates
			else:
				print "date not found, try a proper date. date not changed"
			db.session.add(event)
			db.session.commit()
			return redirect(url_for('events'))
		else:
			print "Event must have a name"
			return
	else: 
		return render_template('eventinfo.html', event=event)

# function to check if 2nd date is after first 
def checkDates(year1, month1, date1, year2, month2, date2):
	if year2 > year1:
		return True
	elif year2 == year1:
		if month2 > month1:
			return True
		elif month2 == month1:
			if date2 > date1:
				return True
			else:
				return False
		else:
			return False
	else: 
		return False

# function to return the next date
def getNextDate(year, month, date):
	daysInMonth = getDaysInMonth(month, year)
	if date < daysInMonth:
		date += 1
	elif date==daysInMonth:
		date = 1
		if month==12:
			year += 1
			month = 1
		else:
			month += 1
	else:
		print "date given/below is larger than the amount of days in this month"
		print year, month, date
		return
	return year, month, date

def getDaysInMonth(month, year):
	if month < 1 or month > 12:
		print "month needs to be between from 1 to 12"
		print month
		return month
	elif month == 2:
		if year%4 == 0:
			if year%100 == 0 and year%400 == 0:
				return 29
			elif year%100 == 0:
				return 28
			else:
				return 29
		else: return 28
	elif month in [4, 6, 9, 11]:
		return 30
	else:
		return 31

## For running website on localhost:5000 in debug mode (automatic refresh of webserver on file save)
if __name__ == '__main__':
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)

