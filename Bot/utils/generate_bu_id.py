import random
from db.db_utils import user_exists


def generate_id():
    while True:
        new_id = random.randint(1000000, 9999999)
        if user_exists(id=new_id, bu_id=True):
            contiune
        else:
            return new_id
