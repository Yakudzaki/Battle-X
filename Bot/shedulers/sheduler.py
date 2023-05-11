from apscheduler.schedulers.asyncio import AsyncIOScheduler
from shedulers.tasks import *

scheduler = AsyncIOScheduler()


#scheduler.add_job(time, 'interval', seconds=10) 

#scheduler.start()

# scheduler.add_job(example, 'data', seconds=10)