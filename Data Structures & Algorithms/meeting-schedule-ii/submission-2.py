"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import attrgetter
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=attrgetter('start'))

        endTime = []
        rooms = 0
        for each in intervals:
            if len(endTime) and endTime[0] <= each.start:
                heapq.heappop(endTime)
                heapq.heappush(endTime, each.end)
            else:
                rooms += 1
                heapq.heappush(endTime, each.end)

        return rooms