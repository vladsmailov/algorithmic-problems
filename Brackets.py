"""
Задача:
Опеределить, является ли последовательность скобочек правильной или нет.
В случае правильной последовательности вывести 1, неправильной -1.
"""
testcases = ['{([])}', '({)}', '({})[]']


def brackets_checker(brackets):
    while '()' in brackets or '{}' in brackets or '[]' in brackets:
        brackets = brackets.replace('()', '').replace('{}', '').replace('[]', '')
    if len(brackets) == 0:
        return 1
    return -1


for test in testcases:
    print(brackets_checker(test))