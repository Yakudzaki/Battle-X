import random

def calculate_ratio(count_mine, guessed):
    percent = guessed / (25 - count_mine) * 100
    if percent <= 10:
        return 0
    elif 10 < percent <= 25:
        return 0.5
    elif 25 < percent <= 40:
        return 1
    elif 40 < percent <= 55:
        return 1.5
    elif 55 < percent <= 65:
        return 2
    elif 65 < percent <= 90:
        return 2.5
    elif 90 < percent:
        return 3


def generate(count):
    count = int(count)
    if count < 3 or count > 24:
        print('Error: Invalid count bombs')
        return 
    field = [random.randint(0, 1) for i in range(25)]
    count_bomb = field.count(1)
    if count_bomb < count:
        while field.count(1) < count:
            index = random.randint(0, 24)
            elem = field[index]
            if elem == 0:
                field[index] = 1
            else:
                pass
    elif count_bomb > count:
        while field.count(1) > count:
            index = random.randint(0, 24)
            elem = field[index]
            if elem == 1:
                field[index] = 0
            else:
                pass
    return field
