from peewee import *
from .models import Users


def create_user(id, bu_id):
    user = Users.create(
        id = id,
        bu_id = bu_id
    )

def user_exists(id, bu_id=False):
    if bu_id:
        return Users.select('bu_id').where(Users.id == id).exists()
    return Users.select('id').where(Users.id == id).exists()



def get_user(id):
    user = Users.select().where(Users.id == id).get()
    return user

def deposite_user_balance(id, sum):
    balance = get_user(id).balance
    new_balance = balance + sum
    Users.update(balance=new_balance).where(Users.id == id).execute()

def get_all_balance():
    sp = [user.balance for user in Users.select()]
    return sum(sp)

def get_count_users():
    return Users.select().count()

def add_ref_level(id):
    referrals_lvl = get_user(id).referrals
    Users.update(referrals=referrals_lvl + 1).where(Users.id == id).execute()

