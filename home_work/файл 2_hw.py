def task_1() -> None:
    # создаем 5 переменных с разными типами
    my_int = 25  # int
    my_float = 99.99  # float
    my_str = "Анна"  # str
    my_list = [1, 2, 3]  # list
    my_bool = True  # bool

    # выводим тип каждой переменной в консоль
    print(type(my_int))
    print(type(my_float))
    print(type(my_str))
    print(type(my_list))
    print(type(my_bool))


# вызываем функцию
task_1()


def task_2() -> None:
    # создаем список
    a = [1, 2, 3, 5, 8, 13, 21]

    # выводим первые 3 значения списка
    print(a[0:3])


# вызываем функцию
task_2()

# * Эта последовательность чисел называется: числа Фибоначчи

def task_3(x: int) -> int:
    # возвращаем квадрат числа
    return x ** 2


# распечатываем вызов функции
print(task_3(7))