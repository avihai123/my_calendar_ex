import calendar
import datetime
from bottle import run, route, template

my_calendar = calendar.HTMLCalendar(calendar.SUNDAY)
now = datetime.datetime.now()


def month_navigation(year, month):
    current_date = datetime.date(year, month, day=15)
    month_delta = datetime.timedelta(30)
    next_month = (current_date + month_delta).month
    prev_month = (current_date - month_delta).month
    return {'prev': '{}/{}'.format(year, prev_month),
            'next': '{}/{}'.format(year, next_month)
            }


@route("/")
def index():
    return month_view(now.year, now.month)


@route('/<year:int>/<month:int>/')
def month_view(year, month):
    month_nav = month_navigation(year, month)
    return template('calendar', calendar=my_calendar.formatmonth(year, month), **month_nav)


@route("/<year:int>/")
def year_view(year):
    return template('calendar', calendar=my_calendar.formatyear(year), prev=year - 1, next=year + 1)


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)
