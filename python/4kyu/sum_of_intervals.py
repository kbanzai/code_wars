# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    if not intervals: return 0
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    interval1 = sorted_intervals[0]
    sum_intervals = 0
    for interval2 in sorted_intervals[1:]:
        if interval1[1] >= interval2[0]:
            interval1 = (interval1[0], max(interval1[1], interval2[1]))
        else:
            sum_intervals += interval1[1] - interval1[0]
            interval1 = interval2
    sum_intervals += interval1[1] - interval1[0]
    return sum_intervals