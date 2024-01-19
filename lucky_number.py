"""
Задача:
Определить, считается ли число счастливым.
Счастливое число - то число сумма квадратов составляющих его чисел в бесонечном цикле приведет к единице.
"""
testcases = [19, 20, 222, 100]

def lucky_number(testcase):
    string_number = str(testcase)
    result = 0
    for digit in string_number:
        result += int(digit) ** 2
    while True:
        if result == 1:
            return "lucky"
        elif string_number == str(result) or result == 20:
            return "unlucky"
        temp = 0
        for digit in str(result):
            temp += int(digit)**2
        result = temp


# for i in testcases:
#     print(lucky_number(i))


"""
Алгоритм из журнала КОД.
Написан с ошибкой, не отработает при зацикливании на числе отличном от исходного!
"""

# считаем сумму квадратов цифр числа
def squared(n):
    result = 0
    while n > 0:
        last = n % 10
        result += last * last
        n = n//10
    print(result)
    return result


def isHappy(n):
    start = n
    result = 0
    while result != 1:
        result = squared(n)
        n = result
        if result == start or result == 20:
            print('Всё зациклилось')
            return False
    return True


if isHappy(21):
    print('Это счастливое число')
else:
    print('Это не счастливое число')