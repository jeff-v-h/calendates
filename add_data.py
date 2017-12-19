from database_setup import db, Date, Event, event_dates


#function to add dates for whole year. Input the year and the day for the 1st of that year (eg. 'Monday')
def createMonthsForYear(year, day):
	for x in range(1, 13):
		day = createDatesForMonth(year, (x), day)
	print "Added year " + str(year)

#function to add dates for each month, Must input the day for the 1st of that month
#returns the day for the first of the next month
def createDatesForMonth(year, month, day):
	month_name = getMonthName(month)
	days_in_month = getDaysInMonth(month, year)
	for x in range(1, days_in_month+1):
		dateToAdd = Date(year=year, month=month, month_name=month_name, date=(x), day=day)
		db.session.add(dateToAdd)
		db.session.commit()
		day = getNextDay(day)
	return day

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

#helper method to get next day
def getNextDay(day):
	if day == 'Monday':
		return 'Tuesday'
	elif day == 'Tuesday':
		return 'Wednesday'
	elif day == 'Wednesday':
		return 'Thursday'
	elif day == 'Thursday':
		return 'Friday'
	elif day == 'Friday':
		return 'Saturday'
	elif day == 'Saturday':
		return 'Sunday'
	elif day == 'Sunday':
		return 'Monday'

#helper mthod to get the month name based on number
def getMonthName(month):
	if month == 1:
		return 'January'
	elif month == 2:
		return 'February'
	elif month == 3:
		return 'March'
	elif month == 4:
		return 'April'
	elif month == 5:
		return 'May'
	elif month == 6:
		return 'June'
	elif month == 7:
		return 'July'
	elif month == 8:
		return 'August'
	elif month == 9:
		return 'September'
	elif month == 10:
		return 'October'
	elif month == 11:
		return 'November'
	elif month == 12:
		return 'December'

''' Functions to create Events once Dates have been added '''
def createPublicHolidays2018():
	newYearsDayDate = Date.query.filter_by(year=2018, month=1, date=1).one()
	newYearsDay = Event(name="New Year's Day", description='The day after the new year.', country='England', city='London')
	newYearsDayDate.events.append(newYearsDay)
	newYearsDay.dates.append(newYearsDayDate)
	db.session.add(newYearsDay)

	goodFriDate = Date.query.filter_by(year=2018, month=3, date=30).one()
	goodFri = Event(name="Good Friday", description='Friday for Easter', country='England', city='London')
	goodFriDate.events.append(goodFri)
	goodFri.dates.append(goodFriDate)
	db.session.add(goodFri)

	easterMonDate = Date.query.filter_by(year=2018, month=4, date=2).one()
	easterMon = Event(name='Easter Monday', description='The Monday during Easter', country='England', city='London')
	easterMonDate.events.append(easterMon)
	easterMon.dates.append(easterMonDate)
	db.session.add(easterMon)

	earlyMayBankDate = Date.query.filter_by(year=2018, month=5, date=7).one()
	earlyMayBank = Event(name='Early May Bank Holiday', description='Bank holiday for early May', country='England', city='London')
	earlyMayBankDate.events.append(earlyMayBank)
	earlyMayBank.dates.append(earlyMayBankDate)
	db.session.add(earlyMayBank)

	springBankDate = Date.query.filter_by(year=2018, month=5, date=28).one()
	springBank = Event(name='Spring Bank Holiday', description='Bank holiday for Spring', country='England', city='London')
	springBankDate.events.append(springBank)
	springBank.dates.append(springBankDate)
	db.session.add(springBank)

	summerHolDate = Date.query.filter_by(year=2018, month=8, date=27).one()
	summerHol = Event(name='Summer Bank Holiday', description='A public holiday in Summer for banks', country='England', city='London')
	summerHolDate.events.append(summerHol)
	summerHol.dates.append(summerHolDate)
	db.session.add(summerHol)

	xmasDayDate = Date.query.filter_by(year=2018, month=12, date=25).one()
	xmasDay = Event(name='Christmas Day', description='Christmas is here!', country='England', city='London')
	xmasDayDate.events.append(xmasDay)
	xmasDay.dates.append(xmasDayDate)
	db.session.add(xmasDay)

	boxingDayDate = Date.query.filter_by(year=2018, month=12, date=26).one()
	boxingDay = Event(name='Boxing Day', description='The day after Christmas', country='England', city='London')
	boxingDayDate.events.append(boxingDay)
	boxingDay.dates.append(boxingDayDate)
	db.session.add(boxingDay)
	db.session.commit()
	print "Added 2018 London public holidays."


print "Adding data to database..."
createMonthsForYear(2018, 'Monday')
createMonthsForYear(2019, 'Tuesday')
createPublicHolidays2018()
print "Completed."