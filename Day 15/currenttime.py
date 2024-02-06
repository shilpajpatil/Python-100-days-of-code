from datetime import *

import pytz


def time():
    tz_INDIA = pytz.timezone('asia/kolkata')

    datetime_INDIA = datetime.now(tz_INDIA)
    print("INDIA time:", datetime_INDIA.strftime("%H:%M"))


