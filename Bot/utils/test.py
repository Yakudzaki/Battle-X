import random

def generate(count):
    count = int(count)
    if count < 5 or count > 24:
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