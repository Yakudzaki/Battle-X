import datetime
import os
import re
from dotenv import load_dotenv


load_dotenv()


TOKEN = str(os.getenv("BOT_TOKEN"))
PAYMENT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI1NTFjYzllNC04MzRjLTI5ZjItMmRiZS0wYWMxMjk3YjMwYzIiLCJ0aWQiOiJjZTBlMTUxZS04MGY0LWY0NDEtYzhlNi1iOGUxODRlMjMwZWYifQ.HJ1VXSSS1_yaMaXnVgReX3IS4vzVUQqQVnEjU61631U'


ADMINS = [1644643904, 5614722872, 5548351085]
ADMINS_CHAT = -1001910573122

# Redis configuration

REDIS_HOST = 'localhost'
REDIS_PORT = 6300

# Bot games configuration

sad_smails = ['😔', '😟', '😢', '😥', '😕', '😪', '😿', '🙁', '☹️', '😓']
right_smails = ['🎉', '✅', '🥇', '👏', '👍', '🎊', '🥳', '🍾', '👑', '👌']



football_rate = {
    1: 0,
    2: 0.25, 
    3: 0.5,
    4: 1,
    5: 2
}