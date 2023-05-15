from collections import Counter, defaultdict, deque
import heapq


"""organization ranking"""


employees = [("John", "Manager"), ("Sally", "CTO"), ("Sam", "CEO"),
             ("Drax", "Engineer"), ("Bob", "CFO"), ("Daniel", "Engineer")]

order = [["CTO", "CEO"], ["Manager", "CTO"],
         ["Engineer", "Manager"], ["CFO", "CEO"]]

graph = defaultdict(list)
degree = Counter()

for x, y in order:
    graph[x].append(y)
    degree[y] += 1

d = defaultdict(list)
for name, rank in employees:
    d[rank].append(name)

start = [k for k in graph if k not in degree]
q = deque(start)

"""
q = [Engineer,CFO]
output = [(Drax,Engineer), (Daniel,Engineer)]
"""
output = []

while q:
    role = q.popleft()
    output += [(x, role) for x in d[role]]
    for emps in graph[role]:
        degree[emps] -= 1
        if degree[emps] == 0:
            q.append(emps)

# print(output[::-1])

a = {}

a["ik"] = [1, 2]
a["ik"][0] = 12


a["james"] = [10, 20]
print(a)


"""
graph = {'CTO': ['CEO'], 'Manager': ['CTO'], 'Engineer': ['Manager'], 'CFO': ['CEO']}
d =  {'Manager': ['John'], 'CTO': ['Sally'], 'CEO': ['Sam'], 'Engineer': ['Drax', 'Daniel'], 'CFO': ['Bob']}
degree = {'CEO': 2, 'CTO': 1, 'Manager': 1}
"""
