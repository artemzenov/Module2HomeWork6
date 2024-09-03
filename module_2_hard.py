import random


def search(number):
    result = str()
    for first_number in range(1, number):
        for second_number in range(first_number + 1, number):
            if number % (first_number + second_number) == 0:
                result += f'{first_number}{second_number}'
    return result


num = random.choice(range(3, 21))
print(f'{num} - число из первой вставки')
print(f'{search(num)} - нужный пароль')