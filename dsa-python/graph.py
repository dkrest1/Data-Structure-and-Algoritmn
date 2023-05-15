
from string import ascii_lowercase
import heapq
from collections import defaultdict, deque
import random
from typing import Collection, Counter, Deque, OrderedDict
nums_node = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), [2, 3], (3, 4)]


class Graph:
    def __init__(self, nums_nodes, edges) -> None:
        self.nums_node = nums_node
        self.data = [[] for _ in range(nums_node)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self) -> str:
        return "\n".join(["{} : {}".format(node, neighbours) for node, neighbours in enumerate(self.data)])

    def __str__(self) -> str:
        return self.__repr__()


graph1 = Graph(nums_node, edges)


def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    discovered[root] = True
    queue.append(root)
    i = 0

    while i < len(queue):
        current = queue[i]
        i += 1
        for node in graph.data[current]:
            if not discovered[node]:
                discovered[node] = True
                queue.append(node)
    return queue


# 0 - 1,4
# 1 - 0,2,3,4,
# 2 - 1,3
# 3 - 1,2,4
# 4 - 0,1,3


class Graph:
    def __init__(self, num_nodes, edges) -> None:
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(nums_node)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self) -> str:
        return "\n".join(["{}: {}".format(node, neighbours) for node, neighbours in enumerate(self.data)])

    def __str__(self) -> str:
        return self.__repr__()


graph2 = Graph(nums_node, edges)


def bfs(graph, root):
    queue = []
    visited = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)
    queue.append(root)
    visited[root] = True
    distance[root] = 0

    idx = 0
    while idx < queue:
        n = queue[idx]
        idx += 1

        for node in graph.data[root]:
            if not visited[node]:
                visited[node] = True
                distance[node] = 1 + distance[n]
                parent[node] = n
                queue.append(node)
    return queue


def dfs(graph, root):
    stack = []
    visited = [False] * len(graph.data)
    result = []

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)

            for nodes in graph.data[root]:
                stack.append(nodes)

    return stack


heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 30)
heapq.heappush(heap, 40)
heapq.heappush(heap, 5)

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]

store = {"ik": 2, "uju": 5, "gozie": 8, "nneka": 6, "too": 10}

res = []
for x in sorted(store.values()):
    res.append(store[x])
print(res)
