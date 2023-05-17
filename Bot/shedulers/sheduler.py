import datetime
import re
from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()
time_dict = {
    'd': 'days', 'day': 'days', 'days': 'days',
    'h': 'hours', 'hour': 'hours', 'hours': 'hours',
    'm': 'minutes', 'mi': 'minutes', 'minutes': 'minutes'}

def time(time_str='1h 10m'):
    time_delta = datetime.datetime.now()
    print(scheduler.get_job('pon').triggered_runs)
    try:
        for time in time_str.split():
            time_value = int(re.findall(r'\d+', time)[0])
            time_unit = time_dict[re.findall(r'[a-z]+', time)[0]]
            time_delta += datetime.timedelta(**{time_unit: time_value})
        print([time_delta, True])
    except:
        return print([None, False])

scheduler.add_job(time, 'interval', seconds=5, name='pon', id='pon') 

scheduler.start()

