from copy import deepcopy
import heapq


def quick_sort(list):
    if len(list) <= 1:
        return list

    else:
        pivot = list[0]
        less_than_pivot = []
        greater_than_pivot = []

        for number in list[1:]:
            if number <= pivot:
                less_than_pivot.append(number)
            else:
                greater_than_pivot.append(number)

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


alist = [1, 6, 3, 2, 4, 3, 5]
# print(quick_sort(alist))

topK = heapq.nsmallest(2, alist)

res = [10, 5, 70]
heap = []
for num in res:
    heapq.heappush(heap, num)

heapq.heappop(heap)

# print(heap)


