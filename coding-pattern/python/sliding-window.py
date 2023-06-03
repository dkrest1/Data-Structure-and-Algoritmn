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
