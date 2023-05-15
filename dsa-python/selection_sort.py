def selection_sort(list):
    l = []

    for i in range(0, len(list)):
        min_index = index_of_min(list)
        l.append(list.pop(min_index))

    return l


def index_of_min(list):
    min_index = 0
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    return min_index


alist = []
# print(selection_sort(alist))

