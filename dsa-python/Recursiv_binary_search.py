from operator import truediv


def recursive_binary(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary(list[midpoint + 1:], target)
        else:
            return recursive_binary(list[:midpoint], target)


def recursive_binary2(list, lp, hp, target):
    if lp > hp:
        return "Value not found"

    mid = (lp + hp) // 2

    if list[mid] == target:
        return mid

    if list[mid] < target:
        return recursive_binary2(list, mid+1, hp, target)
    else:
        return recursive_binary2(list, lp, mid-1, target)


def verify(result):
    print("Target can be found", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary2(numbers, 0, len(numbers)-1, 9)
verify(result)

###############################################################################################
