import random


def bogo_sort(list):
    while not is_sorted(list):
        random.shuffle(list)
    return list


def is_sorted(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


alist = [5, 4, 3, 2, 1]
print(bogo_sort(alist))
