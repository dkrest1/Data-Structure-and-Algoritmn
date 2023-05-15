alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(lp, hp, condition):
    while lp <= hp:
        mid = (lp + hp) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hp = mid - 1
        else:
            lp = mid + 1
    return -1


def count(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return "left"
            else:
                return "found"
        elif cards[mid] < query:
            return "right"
        else:
            return "left"
    return binary_search(0, len(cards) - 1, condition)


res = count(alist, 9)
print(res)
