def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def binon(x, n):
    sum = 1
    factor = 1
    for i in range(1, n + 1):
        factor *= (n - i + 1)
        sum += factor * pow(x, i) / factorial(i)
    return sum


def check_correct_int_input():
    correct_integer = None
    while not correct_integer:
        try:
            correct_integer = int(input())
        except:
            print('Wrong input. This must be an integer')
    return correct_integer


def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def check_terms(old_list):
    new_list = []
    for value in old_list:
        if value % 3 == 0 or value % 5 == 0 or value % 7 == 0:
            new_list.append(value)
            old_list.remove(value)
    return
