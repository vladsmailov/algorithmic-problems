def scoreOfString(s):
    result = 0
    for index in range(1, len(s)):
        result += abs(ord(s[index-1])-ord(s[index]))
    return result

s = 'hello'
print(scoreOfString(s))