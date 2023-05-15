from typing import OrderedDict


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:

            return f"The value is at {midpoint}"
        elif list[midpoint] > target:
            last = midpoint
        else:
            first = midpoint + 1
    return None


def verify(result):
    if result == None:
        return "Target is not in list"
    else:
        return "Target is in the list"


# alist = [1, 2, 3, 4, 5]
# result = binary_search(alist, 2)
# print(result)

store = OrderedDict()

store[1] = 'ik'
store[5] = 'john'
store[8] = 'jacob'
store[0] = 'yan'

print(store.popitem(last=False))

# best case = O(1)
# worst case = O(logn)
#####################################################################################
