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


# time complexity: O(n)
result5 = findLongestSubString("cbbebi", 3)
print("longestSubString", result5)


# ///////////////////////////////////////////// FRUITS INTO BASKET /////////////////////////////////////////////////////////////////////////////
# PROBLEM STATEMENT
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_in_basket(fruitsArr):
    max_length = 0
    start = 0
    fruit_frequency = {}
    for i in range(len(fruitsArr)):
        right_fruit = fruitsArr[i]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while (len(fruit_frequency)) > 2:
            left_fruit = fruitsArr[start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            start += 1
        max_length = max(max_length, i - start + 1)
    return max_length

# time complexity: O(n)


result6 = fruits_in_basket(['A', 'B', 'C', 'B', 'B', 'C'])
print("fruits in a basket =", result6)

# ////////////////////////////////////////////// NO REPEAT SUBSTRING //////////////////////////////////////////
# Problem Statement #
# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".


def max_no_repeatin_subString(str):
    maxLength = 0
    start = 0
    obj = {}
    for i in range(len(str)):
        right_string = str[i]
        if right_string in obj:
            start = max(start, obj[right_string] + 1)
        obj[right_string] = i
        maxLength = max(maxLength, i - start + 1)
    return maxLength

# time complexity = O(n)


result7 = max_no_repeatin_subString("abccde")
print("max_of_no_repeating_substring =", result7)


# //////////////////////////////////////////// Longest Substring with Same Letters after Replacement //////////////////////

# Problem Statement #
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="c", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
def longest_sub_string_with_same_letter_after_replacement(str, k):
    start = 0
    max_length = 0
    max_repeated_letter_count = 0
    obj = {}

    for i in range(len(str)):
        right_str = str[i]
        if right_str not in obj:
            obj[right_str] = 0
        obj[right_str] += 1
        max_repeated_letter_count = max(
            max_repeated_letter_count, obj[right_str])

        if(i - start + 1 - max_repeated_letter_count > k):
            left_str = str[start]
            obj[left_str] -= 1
            start += 1
        max_length = max(max_length, i - start + 1)
    return max_length
# time complexity  = O(n)


result8 = longest_sub_string_with_same_letter_after_replacement("c", 1)
print("Longest_sub_string_with_same_letter_after_replacement =", result8)

# ///////////////////////////////////////// Longest Subarray with Ones after Replacement //////////////////////////
#
# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.


def longest_subArray_with_ones_replacement(arr, k):
    max_length, max_one_count = 0, 0
    start = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            max_one_count += 1
        if(i - start + 1 - max_one_count) > k:
            if arr[start] == 1:
                max_one_count -= 1
                start += 1
        max_length = max(max_length, i - start + 1)
    return max_length


result9 = longest_sub_string_with_same_letter_after_replacement(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)
print("longestSubStringWithSameLetterAfterReplacement =", result9)

# /////////////////////////////////// CHALLENGE ///////////////////////////////////
# ///////////////////////////////// Permutation in a String ///////////////////////////////
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have
# !
# n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.


def permutation_in_a_string(str, ptn):
    start = 0
    obj = {}
    for i in range(len(str)):
        right_string = str[i]
        if right_string not in obj:
            obj[right_string] = 0
        obj[right_string] += 1
