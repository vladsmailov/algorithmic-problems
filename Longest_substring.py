"""
Задача:
Найти длину самой длинной подстроки в строке.
"""
testcases = ['abcabcbb', 'bbbbb', 'pwkkwe', 'dwcuievnuindinuewhddhaskj']


def substring(text):
    substrings_count = len(text)
    results = []
    for index in range(substrings_count):
        results.append([])
        for letter in text[index:]:
            if letter not in results[index]:
                results[index].append(letter)
            else:
                break
    results = sorted(results, key=len, reverse=True)
    return len(results[0])

for item in testcases:
    print(substring(item))

