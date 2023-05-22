import datetime
import re
from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()
time_dict = {
    'd': 'days', 'day': 'days', 'days': 'days',
    'h': 'hours', 'hour': 'hours', 'hours': 'hours',
    'm': 'minutes', 'mi': 'minutes', 'minutes': 'minutes'}


scheduler.start()

