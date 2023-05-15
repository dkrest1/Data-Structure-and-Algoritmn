def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(result, list):
    if result == None:
        return "The target is not in the list"
    else:
        target = list[result]
        return "{} can be found in the list".format(target)


alist = [1, 2, 3, 4, 5]
result = linear_search(alist, 4)
print(verify(result, alist))


# time complexity
# best case = O(1)
# worst case = O(n)
# space complexity
# O(1)
#################################################################
