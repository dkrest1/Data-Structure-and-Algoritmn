"""Question:
Given Parameters:
    Points  = [3.5, 10, 5, 6, 5, 19, 2.3]
    Boundaries = [0, 5, 10, 20, 25, 29]
Return:
    result = [2, 3, 2, 0, 0]

Explanations on how the result was achieved:
result[0] => from Points, we have 2 numbers (i.e, 2.3 and 3.5) that lies between boundary 0 and 5
result[1] => from Points, we have 3 numbers (i.e, 5, 5,and 6) that lies between boundary 5 and 10
result[2] => from Points,  we have 2 numbers (i.e, 10 and 20) that lies between boundaries 10 and 20
result[3] => from Points, we have no numbers lies between boundaries 20 and 25
result[4] => from Points, we have no numbers lies between boundaries 25 and 29

Follow up:
Say we have 
Points  = [0, 0.02, 0.002, 0.22, ..., 1000, ...]
Boundaries = [200, 600]
How can we optimize?
The answer I gave was that I would binary search (instead of linear search) on the Points array to get the start and end boundary index (i.e, where can I start searching 200 from and where would 600 ends) before traversing through the Points array."""

"""
Given Parameters:
    Points  = [3.5, 10, 5, 6, 5, 19, 2.3]
                                        ^               

    
Boundaries = [0, 5, 10, 20, 25, 29]
                  l  r
Return:
    result = [2, 3, 2, 0, 0]
"""


def result(points, boundaries):
    res = []

    # O(n * m) - n is len of boundaries, m is len of points
    for i in range(len(boundaries)-1):
        count = 0
        for point in points:
            if boundaries[i] <= point < boundaries[i+1]:
                count += 1
        res.append(count)
    return res


points = [3.5, 10, 5, 6, 5, 19, 2.3]
boundaries = [0, 5, 10, 20, 25, 29]


print(result(points, boundaries))
# print(round(3.5))


nums = [0, 4, 6, 9, 10, 40, 30, 56, 68, 79, 32, 48, 54, 60, 62, 70, 80]
interval = [30, 60]

nums.sort()
# print(nums)


# binary search on interval to get index
ress = []
for num in interval:
    lp, hp = 0, len(nums) - 1
    while lp <= hp:
        mid = (lp+hp)//2
        if nums[mid] == num:
            ress.append(mid)
            break
        elif nums[mid] < num:
            lp = mid + 1
        else:
            hp = mid - 1

newNums = nums[ress[0]:ress[1] + 1]
# print(ress)
# print(newNums)
