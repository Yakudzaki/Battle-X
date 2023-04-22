from peewee import *
from .models import Users


def create_user(id):
    user = Users.create(
        id = id
    )

def user_exists(id):
    return Users.select('id').where(Users.id == id).exists()

def get_all_balance():
    sp = [user.balance for user in Users.select()]
    return sum(sp)

def get_count_users():
    return Users.select().count()
