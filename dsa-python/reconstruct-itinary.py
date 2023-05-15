from collections import defaultdict, deque


def findItinerary(tickets):
    store = defaultdict(list)
    for ticket in tickets:
        store[ticket[0]].append(ticket[1])
    print(store)

    for orig, dest in store.items():
        dest.sort(reverse=True)
    print(store)

    res = []

    def dfs(node):
        while store[node]:
            dfs(store[node].pop())
        res.append(node)
    dfs("JFK")
    print(res)
    return res[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(findItinerary(tickets))

"""
 graph = {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']}
=
"""
