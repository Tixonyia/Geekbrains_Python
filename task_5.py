from functools import reduce

list_number = [k for k in range(100, 1001, 2)]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, list_number))