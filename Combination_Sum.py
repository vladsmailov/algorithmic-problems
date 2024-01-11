testcase = [2, 3, 6, 7]
target = 7
    result.append(testcase[0])
    if sum(result) >= target:
        print(result)
        return result
    elif
    else:
        combination(testcase, target, result)
        combination(testcase[1:], target, result)


def combination(testcase, target, result):
        combination(testcase[1:], target, [])


print(combination(testcase, target, []))