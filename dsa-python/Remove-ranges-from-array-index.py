'''
                                             |
Input: array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
Output: [-8, 3, -5, 29, 43, 76, 73, 76]

maxSize = 16
lookUpArr = [0,0,0,1,0,1,-1,0,-1,0,1,0,0,-1,0,0,0]

sumSoFar = 1
res = [-8,3,-5,]
'''


array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]

# EFFICIENT O(M + N) where M is length of ranges and N is lenght of range


def removeRange(array, ranges):
    res = []
    lookupArr = [0] * len(array)

    for start, end in ranges:
        if start < len(array):
            lookupArr[start] += 1
        if end < len(array):
            lookupArr[end] -= 1

    count = 0

    for i, num in enumerate(array):
        if lookupArr[i] != 0:
            count += lookupArr[i]
            if count == 0:
                res.append(num)
    return res


# BRUTE FORCE O(M*N) where M is length of ranges and N is lenght of range
# def removeRange(array, ranges):
#     for start, end in ranges:
#         if start > len(array):
#             continue
#         for i in range(start, end):
#             array[i] = 0

#     return [num for num in array if num != 0]


print(removeRange(array, ranges))
