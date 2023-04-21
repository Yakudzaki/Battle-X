from peewee import *
import datetime

# Создание базы данных 
db = SqliteDatabase('utils/db/database.db')

# Создание модели с DateTimeField
class Users(Model):
    id = IntegerField(unique=True, null=False, primary_key=True)
    nickname = CharField(20)
    balance = IntegerField(null=False, default=0)
    referrals = IntegerField(null=False, default=0)
    num_of_games = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        
# Сохранение записи

db.create_tables([Users])
print('yes')