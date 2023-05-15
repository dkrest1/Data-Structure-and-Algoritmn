"""
Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.

Example 1:

Input: 10
Output: 6
Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
6 steps required, as we have used 5 multiplications by 2, and one division by 3.
Example 2:

Input: 3
Output: 7
Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.
"""

from collections import deque
"""
num = 8
step = 3

q = [(10,6),(64,6)]
visited = {0,2,4,1,8,16,32,10,64}
"""


def minStep(n):
    q = deque([(1, 0)])
    visited = set()
    while q:
        size = len(q)
        for _ in range(size):
            num, step = q.popleft()

            if num == n:
                return step

            if num//3 not in visited:
                visited.add(num)
                q.append((num//3, step+1))

            if num*2 not in visited:
                visited.add(num*2)
                q.append((num*2, step+1))


print(minStep(3))
