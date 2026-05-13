# Задание 1: Наибольшее из двух чисел
def max_number(a, b):
    if a > b:
        print(a)
    else:
        print(b)

max_number(25, 13)


# Задание 2: Отличаются ли числа на 135
def check_difference(a, b):
    if abs(a - b) == 135:
        print("yes")
    else:
        print("No")

check_difference(200, 65)


# Задание 3: Название сезона по номеру месяца
def season(month):
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Некорректный номер месяца")

season(3)


# Задание 4: Все ли числа больше 10
def check_three_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

check_three_numbers(15, 20, 25)


# Задание 6: Количество положительных чисел в списке
def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count = count + 1
    print(count)

count_positive([5, -2, 10, -8, 3])