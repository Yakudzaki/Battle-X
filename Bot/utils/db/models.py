from peewee import *
from datetime import datetime

# Создание базы данных 
db = SqliteDatabase('utils/db/database.db')

# Создание модели с DateTimeField
class Users(Model):
    id = IntegerField(unique=True, null=False)
    bu_id = IntegerField(unique=True, null=False)
    nickname = CharField(20, default='Игрок')
    balance = IntegerField(null=False, default=0)
    level = IntegerField(default=1)
    referrals = IntegerField(null=False, default=0)
    num_of_games = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.now)
    
    class Meta:
        database = db
        table_name = 'Users'


class Promocode(Model):
    id = PrimaryKeyField(unique=True, null=True)
    code = CharField(30, null=False)
    count_activate = IntegerField(null=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db

db.create_tables([Promocode])