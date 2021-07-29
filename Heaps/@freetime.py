from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Employee:
    def __init__(self, interval, empIndex, intervalIndex):

        self.interval = interval

        # working hours
        self.empIndex = empIndex
        # for accessing the start and the end time of the empoloyee
        self.intervalIndex = intervalIndex # index of interval in Employee list

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def freeTime(intervals):
    if intervals is None:
        return []

    result, minHeap = [], []

    for i in range(len(intervals)):
        heappush(minHeap, Employee(intervals[i][0], i, 0))


    prev = minHeap[0].interval

    while minHeap:

        popped = heappop(minHeap)
        # if the free time empoloyee ends before the other empoloyee
        if prev.end < popped.interval.start:
            result.append(Interval(prev.end, popped.interval.start))
            prev = popped.interval

        else:
            if prev.end < popped.interval.end:
                prev = popped.interval

        poppedList = intervals[popped.empIndex]
        if len(poppedList) > popped.intervalIndex + 1:
            heappush(minHeap, Employee(poppedList[popped.intervalIndex + 1], popped.empIndex, popped.intervalIndex + 1))
        return result

emp = freeTime([[1,4], [2, 5], [6, 8], [9,12]])
print(emp)
