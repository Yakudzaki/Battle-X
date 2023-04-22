from peewee import *
from .models import Users


def create_user(id):
    user = Users.create(
        id = id
    )

def user_exists(id):
    return Users.select('id').where(Users.id == id).exists()