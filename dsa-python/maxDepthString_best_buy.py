from collections import defaultdict
import unittest
prices = [7, 1, 5, 3, 6, 4]


def bestBuy(prices):
    maxProfit = 0  # maxProfit = 5
    buy = prices[0]  # buy = 1

    for i in range(len(prices)-1):
        if i > 0 and prices[i] > prices[i-1]:
            profit = prices[i] - prices[i-1]
            maxProfit += profit
    return maxProfit


def welcome(name):
    return "Hello {}!!!".format(name)


# print(welcome("Ikechukwu Ejiofor"))

"""
"Given a string, find the deepest string nested inside a '()', '[]' or '{}'."e.g.
'''
"abc(def)ghi" => ["def"]
"abc(def[ghi]jkl)mno" => ["ghi"]
"abc(def)ghi[jkl]mno" => ["def", "jkl"]
"abc" => []
"" => []
(),[],{}
'''
"abc(def[ghi]jkl)mno" => ["ghi"]
            ^
maxDepth = 2
output = []
start_window = 7
curr = 2


subs = ""
"""


def maxDepthString(s: str) -> list:
    max_depth = 0
    output = []
    open_brackets = {"(": ")", "{": "}", "[": "]"}
    closing_brackets = {")", "}", "]"}

    start_window = 0
    curr_depth = 0
    for end_window, c in enumerate(s):
        if c in open_brackets:
            start_window = end_window
            curr_depth += 1
            max_depth = max(max_depth, curr_depth)

        elif c in closing_brackets and c == open_brackets[s[start_window]]:
            if curr_depth == max_depth:
                output.append(s[start_window + 1: end_window])
                curr_depth -= 1

    return output


# print(maxDepthString("a[bc]def{cd}"))


"""
BLOOMBERG TARGET SUM
arr1 = [1,3,4]
          i
arr2 = [2,5,6]
        j  
target = 5   # ans = 3 & 2
"""
arr1 = [1, 3, 4]
arr2 = [2, 5, 6]
target = 100   # ans = 3 & 2


def isTrue(arr1, arr2, target):
    i = 0
    j = len(arr2) - 1
    while i in range(len(arr1)) and j in range(len(arr2)):
        sum = arr1[i] + arr2[j]
        if sum == target:
            return True
        elif sum > target:
            j -= 1
        else:
            i += 1
    return False


# print(isTrue(arr1, arr2, target))
print(False or True)
