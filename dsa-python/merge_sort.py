def merge_sort(list):

    if len(list) <= 1:
        return list

    else:
        left_half, right_half = split(list)
        left = merge_sort(left_half)
        right = merge_sort(right_half)

        return merge(left, right)


def split(list):
    mid = len(list)//2
    left = list[: mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) or j < len(right):
        if i < len(left):
            l.append(left[i])
            i += 1
        elif j < len(right):
            l.append(right[j])
            j += 1

        else:
            if left[i] < right[j]:
                l.append(left[i])
                i += 1
            else:
                l.append(right[j])
                j += 1

    return l


# def verify(list, sorted_list):
    return list == sorted_list


def verify(list):
    if len(list) == 0 or len(list) == 1:
        return False

    else:
        return list[0] < list[1] and verify(list[1:])


alist = [10, 9, 8, 7, 6, 5, 3, 7, 1]
#sorted_list = sorted(alist)
# print(sorted_list)


l = merge_sort(alist)
print(l)

# print(verify(l, sorted_list))
print(verify(l))
print(verify(alist))
##########################################################################################
# run time = O(nlogn)
# space complexity = O(n)
