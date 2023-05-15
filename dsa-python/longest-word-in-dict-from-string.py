"""
I "abcdera" -> aaboder "m"
11 ['valid", "lest", "bread",
...] (very long list) -> ["bread", "valid", "lest'", "bad] -> laa*, "abder", "a1

"""
import heapq
from typing import Counter


s = "abcdera"
wordDict = ["valid", "lest", "bread", "bad"]


# print(max(wordDict, key=len))
#    output = []
#         for word in dictionary:
#             i = 0
#             while i < len(word):
#                 if word[i] not in char:
#                     break
#                 i += 1

#             if i == len(word):
#                 output.append(word)

#         heapq.heapify(output)
#         return heapq.heappop(output)

def longestWord(s, list):
    output = []
    char = Counter(s)
    wordDict.sort(key=len, reverse=True)
    for word in wordDict:
        i = 0
        while i < len(word):
            if word[i] not in char:
                break
            i += 1

        if i == len(word):
            output.append(word)
    return heapq.heappop(output)


print(longestWord(s, wordDict))

print(int(3/2))
print(round(3/2))
print(3//2)
# for i in range(len(word)):
#     if word[i] not in char:
#         break
# if i == len(word) - 1:
#     return word
