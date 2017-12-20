from database_setup import db, Date, Event, events_dates
from project import getDaysInMonth

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

	goodFriDate = Date.query.filter_by(year=2018, month=3, date=30).one()
	goodFri = Event(name="Good Friday", description='Friday for Easter', country='England', city='London')
	goodFriDate.events.append(goodFri)

	easterMonDate = Date.query.filter_by(year=2018, month=4, date=2).one()
	easterMon = Event(name='Easter Monday', description='The Monday during Easter', country='England', city='London')
	easterMonDate.events.append(easterMon)

	earlyMayBankDate = Date.query.filter_by(year=2018, month=5, date=7).one()
	earlyMayBank = Event(name='Early May Bank Holiday', description='Bank holiday for early May', country='England', city='London')
	earlyMayBankDate.events.append(earlyMayBank)

	springBankDate = Date.query.filter_by(year=2018, month=5, date=28).one()
	springBank = Event(name='Spring Bank Holiday', description='Bank holiday for Spring', country='England', city='London')
	springBankDate.events.append(springBank)

	summerHolDate = Date.query.filter_by(year=2018, month=8, date=27).one()
	summerHol = Event(name='Summer Bank Holiday', description='A public holiday in Summer for banks', country='England', city='London')
	summerHolDate.events.append(summerHol)

	xmasDayDate = Date.query.filter_by(year=2018, month=12, date=25).one()
	xmasDay = Event(name='Christmas Day', description='Christmas is here!', country='England', city='London')
	xmasDayDate.events.append(xmasDay)

	boxingDayDate = Date.query.filter_by(year=2018, month=12, date=26).one()
	boxingDay = Event(name='Boxing Day', description='The day after Christmas', country='England', city='London')
	boxingDayDate.events.append(boxingDay)

	db.session.commit()
	print "Added 2018 London public holidays."

def addSportEvents2018():
	ausOpen = Event(name='Australian Open', description='The first of four tennis grand slam tournamnets each year held in Australia.', country='Australia', city='Melbourne')
	for x in range(15, 29):
		date = Date.query.filter_by(year=2018, month=1, date=(x)).one()
		ausOpen.dates.append(date)

	commonwealthGames = Event(name='Commonwealth Games', description='Sporting event between elite athletes of countries from the Commonwealth.', country='Australia', city='Gold Coast')
	for x in range(4, 16):
		date = Date.query.filter_by(year=2018, month=4, date=(x)).one()
		commonwealthGames.dates.append(date)

	faCupFinal = Event(name='FA Cup Final', description='The final match of the Football Association Challenge Cup', country='England', city='London')
	date = Date.query.filter_by(year=2018, month=5, date=19).one()
	faCupFinal.dates.append(date)

	uefaChampsFinal = Event(name='UEFA Champions League Final', description='The final game in the UEFA Champions League', country='Ukraine', city='Kiev')
	date = Date.query.filter_by(year=2018, month=5, date=26).one()
	uefaChampsFinal.dates.append(date)

	frenchOpen = Event(name='Roland-Garros', description='Also known as The French Open, this tennis grand slam is held on courts with clay surfaces.', country='France', city='Paris')
	for x in range(27, 32):
		date = Date.query.filter_by(year=2018, month=5, date=(x)).one()
		frenchOpen.dates.append(date)
	for x in range(1, 11):
		date = Date.query.filter_by(year=2018, month=6, date=(x)).one()
		frenchOpen.dates.append(date)

	fifaWorldCup = Event(name='FIFA World Cup', description="The World's most watched global sporting event held every four years.", country='Russia', city='')
	for x in range(14, 31):
		date = Date.query.filter_by(year=2018, month=6, date=(x)).one()
		fifaWorldCup.dates.append(date)
	for x in range(1, 16):
		date = Date.query.filter_by(year=2018, month=7, date=(x)).one()
		fifaWorldCup.dates.append(date)

	nbaFinalsStart = Event(name='NBA Finals (start)', description='The start of the American National Basketball League finals series.', country='USA', city='')
	date = Date.query.filter_by(year=2018, month=5, date=31).one()
	nbaFinalsStart.dates.append(date)
	
	tourDeFrance = Event(name='Tour De France', description='The biggest multistage outdoor cycling competition held in France every year.', country='France', city='')
	for x in range(7, 30):
		date = Date.query.filter_by(year=2018, month=7, date=(x)).one()
		tourDeFrance.dates.append(date)

	wimbledon = Event(name='Wimbledon', description='The last of four tennis grand slam tournamnets each year held in Wimbledon, England.', country='England', city='London')
	for x in range(2, 16):
		date = Date.query.filter_by(year=2018, month=7, date=(x)).one()
		wimbledon.dates.append(date)

	melbourneCup = Event(name='Melbourne Cup', description='A major horse racing event held in Melbourne Australia', country='Australia', city='Melbourne')
	date = Date.query.filter_by(year=2018, month=11, date=6).one()
	melbourneCup.dates.append(date)

	db.session.commit()
	print "Added 2018 sport events."

print "Adding data to database..."
createMonthsForYear(2018, 'Monday')
createMonthsForYear(2019, 'Tuesday')
createPublicHolidays2018()
addSportEvents2018()
print "Completed."