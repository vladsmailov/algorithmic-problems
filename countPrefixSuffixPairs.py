def countPrefixSuffixPairs(words):
    counter = 0
    for index in range(len(words)-1):
        for second_index in range(index+1, len(words)):
            if (words[index] == words[second_index][:len(words[index])] and
                    words[index] == words[second_index][len(words[second_index])-len(words[index]):]):
                counter += 1
    return counter


words = ["abab","ab"]
print(countPrefixSuffixPairs(words))
