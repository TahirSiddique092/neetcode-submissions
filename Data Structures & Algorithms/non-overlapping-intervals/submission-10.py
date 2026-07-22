class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prev = 0
        curr = 1
        count = 0
        intervals.sort()
        while curr < len(intervals):
            if intervals[prev][1] > intervals[curr][0]:
                count += 1
                if intervals[prev][1] > intervals[curr][1]:
                    prev = curr
                    curr += 1
                else:
                    curr +=1
            else:
                prev = curr
                curr += 1
        return count