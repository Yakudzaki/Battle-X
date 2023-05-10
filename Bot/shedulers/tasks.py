"""Функции в этом файлы - таски для APShedler"""
from loader import dp
from data.config import ADMINS
import datetime
import os
import re


async def example():
    print(111)


time_dict = {
    'd': 'days', 'day': 'days', 'days': 'days',
    'h': 'hours', 'hour': 'hours', 'hours': 'hours',
    'm': 'minutes', 'mi': 'minutes', 'minutes': 'minutes'}

def time(time_str='1h 10m'):
    time_delta = datetime.datetime.now()
    try:
        for time in time_str.split():
            time_value = int(re.findall(r'\d+', time)[0])
            time_unit = time_dict[re.findall(r'[a-z]+', time)[0]]
            time_delta += datetime.timedelta(**{time_unit: time_value})
        print([time_delta, True])
    except:
        return print([None, False])
    

