"""
Задача:
Написать три функции сдля суммирования всех элементов массива.
1)С помощью цикла for
2)С помощью цикла while
3)Рекурсией
"""
testcase = [3, 4, 1, 4, 7, 9, 3, 6, 7, 3]


def using_for(testcase):
    result = 0
    for digit in testcase:
        result += digit
    return result


def using_while(testcase):
    index = 0
    result = 0
    while index < len(testcase):
        result += testcase[index]
        index += 1
    return result


def recursion(result, testcase):
    if len(testcase) == 0:
        return result
    return recursion(result+testcase[0], testcase[1:])


print(using_for(testcase))
print(using_while(testcase))
print(recursion(0, testcase))