from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]

        res = []
        found = False
        visited = set()
        return self.bfs(s, res, found, visited)

    def bfs(self, s, res, found, visited):
        q = deque([s])
        visited.add(s)

        while q:
            s = q.popleft()

            if self.isValid(s):
                res.append(s)
                found = True

            if found:
                continue

            for i in range(len(s)):
                if s[i].isalpha():
                    continue
                newString = s[:i] + s[i+1:]
                if newString not in visited:
                    visited.add(newString)
                    q.append(newString)
        return res if res else [""]

    def isValid(self, s):
        count = 0
        for c in s:
            if c.isalpha():
                continue
            elif c == "(":
                count += 1
            elif c == ")":
                count -= 1

            if count < 0:
                return False
        return count == 0


"""
Time Complexity : O(2^N) since in the worst case we will have only left parentheses in the expression
 and for every bracket we will have two options i.e. whether to remove it or consider it. Considering that the expression has N parentheses,
  the time complexity will be O(2^N).
Space Complexity : O(N) because we are resorting to a recursive solution and for a recursive solution there is always stack space used as internal function states are saved onto a stack during recursion.
 The maximum depth of recursion decides the stack space used. Since we process one character at a time and the base case for the recursion is when we have processed all of the characters of the expression string, the size of the stack would be O(N)O(N). Note that we are not considering the space required to store the valid expressions. We only count the intermediate space here.
"""
