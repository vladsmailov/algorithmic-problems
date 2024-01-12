"""
Задача:
Проверить является ли число палиндромом.
Если число - палиндром вернуть 1, если нет - -1.
"""
testcase = 12344321
testcase_nok = 12345621


def palindrome(testcase):
    """Примитивный алгоритм."""
    left = 0
    stack = str(testcase)
    right = len(stack) - 1
    while left < right:
        if stack[left] == stack[right]:
            left += 1
            right -= 1
        else:
            return -1
    return 1


def palindrome_advanced(testcase):
    if str(testcase) == str(testcase)[::-1]:
        return 1
    return -1


def palindrome_without_strings(testcase):
    temp = testcase
    rank = 0
    while temp > 0:
        temp //= 10
        rank += 1
    right = rank - 1
    while right > 0:
        print(testcase//(10**right), testcase%10)
        if testcase//(10**right) == testcase%10:
            testcase -= testcase//(10**right) * 10**right
            testcase //= 10
            right -= 2
        else:
            return -1
    return 1


print(palindrome(testcase))
print(palindrome(testcase_nok))
print(palindrome_advanced(testcase))
print(palindrome_advanced(testcase_nok))
print(palindrome_without_strings(testcase))
print(palindrome_without_strings(testcase_nok))