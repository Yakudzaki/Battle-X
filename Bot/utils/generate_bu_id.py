import random
from .db.db_utils import user_exists


def generate_id():
    new_id = random.randint(1000000, 9999999)
    while user_exists(id=new_id, bu_id=True):
        new_id = random.randint(1000000, 9999999)
    return new_id
