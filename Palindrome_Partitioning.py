testcase = 'aabba'

def solution(testcase):
    result = [[]]
    temp = testcase[0]
    for letter in testcase:
        result[0].append(letter)
        if letter == temp:
            pass

solution(testcase)