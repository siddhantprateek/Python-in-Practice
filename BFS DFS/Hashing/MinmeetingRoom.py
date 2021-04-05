from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __it__(self, other):
        return self.end < other.end

    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x.start)

        rooms = 0
