import math
import sys
# Two Pointers
# /////////////////// Problem Statement /////////////////////
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
# example 1
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# example 2
# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

def pairWithhTargetSum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]

        if current < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

# ////////////////////ALTERNATE SOLUTION


def pairWithTargetSum2(arr, target):
    nums = {}

    for i, num in enumerate(arr):
        if target - num in nums:
            return [nums[target - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


# space complexity O(1)
# time complexity O(N)
result_1 = pairWithhTargetSum([2, 5, 9, 11], 11)
result_2 = pairWithTargetSum2([2, 5, 9, 11], 11)

# /////////////////////////// REMOVE DUPLICATE //////////////////////////////////////////////////////
# Problem Statement
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].


def array_non_duplicate(arr):
    non_duplicate = 1
    i = 1
    while (i < len(arr)):
        if arr[non_duplicate - 1] != arr[i]:
            arr[non_duplicate] = arr[i]
            non_duplicate += 1
        i += 1
    return non_duplicate


result_3 = array_non_duplicate([2, 2, 2, 11])

# /////////////////////////////////////// Make Square of Arr input in sorted order ///////////////////////////////
# problem statement
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

# /////////////////////////////////////// Make Square of Arr input in sorted order ///////////////////////////////
# problem statement


def make_square_of_input_arr(arr):
    n = len(arr)
    squares = [0 for i in range(n)]
    left, right, highestSquareIdx = 0,  n - 1, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    return squares

result_4 = make_square_of_input_arr([-3, -1, 0, 1, 2])

# /////////////////////////////////////// Tripplet Sum of an Array To Zero ///////////////////////////////
# problem statement
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.


def search_tripplet(arr):
   arr.sort()
   tripplet = []
   for i in range(len(arr)):
       
       if i > 0 and arr[i] == arr[i-1]:
           continue
       search_pair(arr, -arr[i], i+1, tripplet)
   return tripplet
       


def search_pair(arr, target_sum, left, tripplet):
    right = len(arr)- 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            tripplet.append([-target_sum, arr[right], arr[left]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1

result_5 = search_tripplet([-3, 0, 1, 2, -1, 1, -2])



#//////////////////////////////// Triplet Sum Close To a Target ////////////////////////////////////////////////
# Problem Statement #
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:

# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:

# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.

def closest_triplet_sum(arr, targetSum):
    #sort arr
    arr.sort()
    closeSum = sys.maxsize
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        while(left < right):
            target_diff = targetSum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return targetSum - target_diff
            
            if abs(target_diff) < abs(closeSum):
                closeSum = target_diff
            
            if target_diff > 0:
                left += 1
            else:
                right -=  1
                
    return targetSum - closeSum

result_6 = closest_triplet_sum([1, 0, 1, 1], 100)


#//////////////////////////////// Triplet With Smaller Sum ////////////////////////////////////////////////
# Problem Statement #
# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

def triplet_less_than_target_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) -2):
        count += search_pair_less(arr,target - arr[i], i)
    return count

def search_pair_less(arr, target_sum, first):
    count = 0
    left , right = first + 1,  len(arr) - 1
    
    while(left < right):
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count

result_7 = triplet_less_than_target_sum([-1, 0, 2, 3], 3)


#//////////////////////////////// Dutch National Flag Problem (medium) ////////////////////////////////////////////////
# Problem Statement #
# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# Example 1:

# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]
# Example 2:

# Input: [2, 2, 0, 1, 2, 0]
# Output: [0 0 1 2 2 2 ]

def dutch_national_flag(arr):
    low, high = 0, len(arr) - 1
    i = 0
    while(i <= high):
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1

def result8(arr):
    dutch_national_flag(arr)
    return arr

result_8 = result8([2, 2, 0, 1, 2, 0])


def main():
    print("example_one: ", result_1)
    print("example_two: ", result_2)
    print("example_three", result_3)
    print("example_4", result_4)
    print("example_5", result_5)
    print("example_6", result_6)
    print("example_7", result_7)
    print("example_8", result_8)

main()