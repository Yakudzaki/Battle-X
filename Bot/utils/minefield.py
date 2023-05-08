import random
from decimal import Decimal

def calculate_ratio(count_mine, guessed):
    percent = guessed / (25 - count_mine) 
    return round(Decimal(str(Decimal(str(round(percent, 2))) * Decimal('3.5'))), 2)



print(calculate_ratio(3, 1))

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
