from apscheduler.schedulers.asyncio import AsyncIOScheduler
from shedulers.tasks import *

scheduler = AsyncIOScheduler()


# scheduler.add_job(example, 'interval', seconds=10) Добавляем таск
# scheduler.add_job(time, 'interval', seconds=5)
scheduler.start()