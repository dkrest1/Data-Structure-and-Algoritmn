"""
A->B
B->C,D
C-E
D-E

allPaths = [[A,B,C,E],]

- write function to add path

- find all posible path from a give source to a destination


Time Complexity: O(V^E). 
The time complexity is polynomial. From each vertex there are E vertices that can be visited from current vertex.
Auxiliary space: O(V^E). 
To store the paths V^E space is needed.
"""
import random
from typing import Counter


store = {"A": ["B"], 'B': ["C", "D", ], "C": ["E"], "D": ["E"], "E": []}


def addStop(source, destination):
    if source not in store:
        store[source] = []
        store[source].append(destination)

    else:
        store[source].append(destination)

    if destination not in store:
        store[destination] = []
    return store


def allPathsFromSourceToTarget(source, destination):
    allPaths = []
    path = [source]
    target = destination
    visited = set()
    findPaths(source, path, target, allPaths, visited)
    return allPaths


def findPaths(source, path, target, allPaths, visited):
    if source == target:
        allPaths.append(list(path))

    #path = [A,]
    # visited = {}
    else:
        for i in store[source]:
            if i not in visited:
                visited.add(i)
                path.append(i)
                findPaths(i, path, target, allPaths, visited)
                path.pop()
                visited.remove(i)


# print(allPathsFromSourceToTarget("A", "E"))

print(addStop('A', 'Z'))
