'''
Задача:
Найти наибольшее общее начало всех слов в списке.
'''
testcase = ['domra', 'domen', 'dom', 'dokument']


def root(testcase):
    """ Простое решение."""
    sorted_list = sorted(testcase, key=len)
    first_word = {index: letter for index, letter in enumerate(sorted_list[0])}
    result = ''
    for index in first_word.keys():
        for word in sorted_list[1:]:
            if word[index] != first_word[index]:
                return result
        result += first_word[index]
    return result


def root_advanced(testcase):
    result = ''
    for letters in zip(*testcase):
        if len(set(letters)) == 1:
            result += letters[0]
        else:
            return result
    return result

print(root_advanced(testcase))