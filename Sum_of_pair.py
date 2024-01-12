"""
Задача:
Вывести ИНДЕКСЫ двух числе, сумма которых равна переменной target.
"""
from datetime import datetime as dt
import time

testcase = (2, 4, 5, 1, 8)
target = 5


def sum_of_pair(testcase, target):
    """ Решение с перебором значений в цикле."""
    start = time.time()
    for index in range(len(testcase)-1):
        for digit in testcase[index:]:
            if target - testcase[index] == digit:
                time_delta = time.time()-start
                return [index, testcase.index(digit), f'Время выполнения={time_delta}']
    return -1

print(sum_of_pair(testcase, target))


def sum_of_pair_advanced(testcase, target):
    start= dt.now()
    digits = {value: index for index, value in enumerate(testcase)}
    for digit in testcase:
        key = target - digit
        if key in digits:
            time_delta = dt.now() - start
            return [digits[digit], digits[key], f'Время выполнения={time_delta.total_seconds()}']
    return -1


print(sum_of_pair_advanced(testcase, target))