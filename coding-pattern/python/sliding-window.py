import math
# Sliding windows
# Question: Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# solving with BRUTE FORCE first


def findAverage(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        _sum = 0
        for j in range(i, k+i):
            _sum += arr[j]
        result.append(_sum/k)
    return result


result = findAverage([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
print(result)

# TIME COMPLEXITY
# (N^2)

# PS this can be improved and reduce this to O(N)

# ================================================ SLIDING WINDOW ===============================


def findAverageSlidingWindow(arr, k):
    result = []
    sum, start = 0, 0
    for i in range(len(arr)):
        sum += arr[i]
        if i >= k - 1:
            result.append(sum/k)
            sum -= arr[start]
            start += 1
    return result
# Time complexity
# O(N)


result = findAverageSlidingWindow([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
print(result)

# Question 2 ////////////////////// MAXIMUM SUM SUB ARRAY OF SIZE K (EASY)
# Problem Statement #
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
arr2 = [2, 1, 5, 1, 3, 2]
k2 = 3
#Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# /////////////////////////////BRUTE FORCE SOLUTION ////////////////////////////////////////////////


def maxSub(arr, k):
    max_sum = 0
    sum = 0
    for i in range(len(arr) - k + 1):
        sum = 0
        for j in range(i, i+k):
            sum += arr[j]
            max_sum = max(max_sum, sum)
    return max_sum


# Big O: O(N^2)
result2 = maxSub(arr2, k2)
print("maxSubArrBruteForce =", result2)

# /////////////////////////////////////////// SLINGING WINDOW ////////////////////////////////////////


def maxSubSlidingWindow(arr, k):
    max_sum = 0
    start, sum = 0, 0
    for i in range(len(arr)):
        sum += arr[i]
        if(i >= k - 1):
            max_sum = max(max_sum, sum)
            sum -= arr[start]
            start += 1
    return max_sum


# Big O:
# Time Complexity: O(n)
# Space Complexity: O(1)
result3 = maxSubSlidingWindow(arr2, k2)
print("maxSubArrSlidingWindow =", result3)


# ///////////////////////////////////////////////////////// SMALLEST SUB ARRAY WITHIN A GIVEN SET ////////////////////////////////////////////////

# QUESTION 3.Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

def findMinLengthSumOfArr(arr, k):
    minLength = math.inf
    _sum, start = 0, 0
    for i in range(len(arr)):
        _sum += arr[i]
        while(_sum >= k):
            minLength = min(minLength, i - start + 1)
            _sum -= arr[start]
            start += 1
    if(minLength == math.inf):
        return 0

    return minLength


# Big O:
# Time Complexity: O(n)
# Space Complexity: O(1)
result4 = findMinLengthSumOfArr([2, 1, 5, 2, 3, 2], 7)
print("minLengthSumOfArr =", result4)

# ///////////////////////////////////////////////// Longest Substring with K Distinct Characters /////////////////////////////////////////
# Problem Statement #
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".


def findLongestSubString(str, k):
    maxSubString = 0
    start = 0
    obj = {}
    for i in range(len(str)):
        char = str[i]
        if char not in obj:
            obj[char] = 0
        obj[char] += 1
        while len(obj) > k:
            char2 = str[start]
            obj[char2] -= 1
            if obj[char2] == 0:
                del obj[char2]
            start += 1
        maxSubString = max(maxSubString, i - start + 1)

    return maxSubString


result5 = findLongestSubString("cbbebi", 3)
print("longestSubString", result5)
