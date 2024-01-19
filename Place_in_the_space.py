"""
Задача:
Написать алгоритм добавления нового пункта в список или вывода сообщения о том, что он присутствует в списке, если он уже есть.
Добавленнный элемент должен располагаться в алфавитном порядке.
"""
# исходный список
testcase = ['арбуз','вишня','дыня','персик','яблоко',]
# новые данные, которые нужно добавить
target = 'киви'

digit_testcae = [1, 3, 4, 5, 6, 7, 8, 9]
digit_target = 2


def binary(testcase, target):
    start = 0
    end = len(testcase)-1
    while start <= end:
        mid = (end + start) // 2
        print(mid)
        if target < testcase[mid]:
            end = mid - 1
        else:
            start = mid + 1
    testcase.insert(end+1, target)
    return testcase

print(binary(testcase, target))
print(binary(digit_testcae, digit_target))
