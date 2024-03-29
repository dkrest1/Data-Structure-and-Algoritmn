
# /////////////////////////////////// Merge Intervals (medium) /////////////////////////////////////////////
# Problem Statement #
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
# one [1,5]

# Example 2:

# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

# Example 3:

# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into on

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end="")


def merge(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals


def result_1():
    print("Merged Interval ", end="")
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged Interval ", end="")
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


# //////////////////////////Insert Interval (medium)/////////////////////////////////////////

# Problem Statement #
# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Example 2:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
# Example 3:

# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

def insert(intervals, new_interval):
    i, start, end = 0, 0, 1
    merged = []

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


result_2 = insert([[2, 3], [5, 7]], [1, 4])


# //////////////////////////////////////////////////// Intervals Intersection (medium) //////////////////////////////////
# Problem Statement #
# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

def merge_intersection(arr1, arr2):
    i, j, start, end = 0, 0, 0, 1
    result = []

    while i < len(arr1) and j < len(arr2):
        a_intersect_b = arr1[i][start] >= arr2[j][start] and arr1[i][start] <= arr2[j][end]
        b_intersect_a = arr2[j][start] >= arr1[i][start] and arr2[j][start] <= arr1[i][end]

        if a_intersect_b or b_intersect_a:
            result.append([max(arr1[i][start], arr2[j][start]),
                          min(arr1[i][end], arr2[j][end])])

        if arr1[i][end] < arr2[j][end]:
            i += 1
        else:
            j += 1

    return result


result_3 = merge_intersection([[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]])

# ////////////////////////////////////////////// Conflicting Appointments (medium) //////////////////////////
# Problem Statement #
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:

# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# Example 2:

# Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.
# Example 3:

# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.




def main():
    result_1()
    print("Insert and merged interval at ", result_2)
    print("Interval intersection", result_3)


main()
