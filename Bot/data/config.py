import datetime
import os
import re
from dotenv import load_dotenv


load_dotenv()


TOKEN = str(os.getenv("BOT_TOKEN"))
PAYMENT_TOKEN = str(os.getenv('PAYMENT_TOKEN'))


ADMINS = ['1644643904']
ADMINS_CHAT = ['-1001910573122']

