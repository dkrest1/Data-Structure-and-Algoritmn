from collections import defaultdict
from unicodedata import name


def smallestNegativeBalance(debts):
    # Write your code here
    """
    devts = [[Alex,Blake,2], [Blake,Alex,2],[Casey,Alex,5], [Blake,casey,7],[Alex,Blake,4],[Alex,casey,4]]
    graph = {Alex: {Blake: 6, casey:4}, Blake: {Alex: 2, casey:7}, casey: {Alex: 5}}]

    names = {Alex,Blake,Casey}

    debtoorMap = {alex: 10,blake: 9, casey:5}

    lenderMap = {alex:7, blake:6, casey:11}

    res = {alex:-3, blake:-3, casey:6}
    """

    debts = [debt.split() for debt in debts]
    # print(debts)
    names = set()
    for borrower, lender, amount in debts:
        names.add(borrower)
    # print(names)
    graph = defaultdict(dict)

    for borrower, lender, amount in debts:
        amount = int(amount)
        if borrower not in graph or borrower in graph and lender not in graph[borrower]:
            graph[borrower][lender] = amount
        elif borrower in graph and lender in graph[borrower]:
            graph[borrower][lender] += amount

    # print(graph)
    debtorMap = {}

    for name in names:
        sum = 0
        if name in graph:
            for lender in graph[name]:
                sum += graph[name][lender]
            debtorMap[name] = sum

    lenderMap = {}
    for name in names:
        sum = 0
        for key in graph:
            if name in graph[key]:
                sum += graph[key][name]
        lenderMap[name] = sum

    res = {}

    for x, y in zip(lenderMap, debtorMap):
        val = lenderMap[x] - debtorMap[y]
        res[x] = val

    # print(res)

    minNum = min(res.values())

    output = []

    if minNum >= 0:
        return ['Nobody has a negative balance']

    for key, val in res.items():
        if val == minNum:
            output.append(key)
    output.sort()

    return output


debts = ['Alex Blake 2', 'Blake Alex 2', 'Casey Alex 5',
         'Blake Casey 7', 'Alex Blake 4', 'Alex Casey 4']

# debts = ['Alex Blake 0', 'Blake Alex 0', 'Casey Alex 0',
#          'Blake Casey 0', 'Alex Blake 0', 'Alex Casey 0']


print(smallestNegativeBalance(debts))
