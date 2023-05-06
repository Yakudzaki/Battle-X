def calculate(count_mine, guessed):
    percent = guessed / count_mine * 100
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

print(calculate(20, 18))