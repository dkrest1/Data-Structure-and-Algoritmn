import collections
from typing import Collection

# Collatz conjecture


def CollatzConjecture(N, visited=set()):

    def isCollatz(N):
        if N == 1:
            return True
        if N in visited:
            return False
        visited.add(N)
        if N % 2 == 0:
            N //= 2
            return isCollatz(N)
        else:
            N = (3*N) + 1
            return isCollatz(N)
    return isCollatz(N)

# ==========================================================================================================================================


"""
Starting with any positive integer N, we define the Collatz sequence corresponding to N as the numbers formed by the following operations:
If N is even, N→ N/2
if N is odd,   N→ 3N+ 1
It is conjectured but not yet proven that no matter which positive integer we start with; we always end up with 1.
For example, 10 → 5  → 16  → 8  → 4  → 2  → 1. You have to give the maximum collatz sequence length among all the numbers from 1 to N(both included).

"""

# Brute Force runtime -> (O(N*2)) , space time -> (O(N))   BFS


def maxCollatLength(N):
    maxLen = 1

    if N == 1:
        return maxLen

    for i in range(2, N+1):
        maxLen = max(maxLen, collat(i))
    return maxLen


def collat(N):
    q = collections.deque([(N, 1)])

    while q:
        size = len(q)
        for _ in range(size):
            num, step = q.popleft()

            if num == 1:
                return step

            if num % 2 == 0:
                num //= 2
            else:
                num = (3 * num) + 1

            q.append((num, step+1))


print(maxCollatLength(10))

# ==========================================================================================================================================

# Optimal Solution runtime -> (O(N)) , space time -> (O(N))


def maxCollatzLength(N):
    steps = [0, 1]

    for i in range(2, N+1):
        count = 0

        while i != 0:
            if i % 2 == 0:
                i //= 2
                count += 1

                if i < len(steps):
                    count += steps[i]
                    break
            else:
                i = (3*i) + 1
                count += 1

                if i < len(steps):
                    count += steps[i]
                    break
        steps.append(count)

    return max(steps)

# ==========================================================================================================================================


# print(maxCollatzLength(10))


# print(maxLenCollatz(10))
