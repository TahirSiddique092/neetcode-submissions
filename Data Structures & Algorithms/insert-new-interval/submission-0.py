class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        afterExists = False
        for idx, interval in enumerate(intervals):
            if interval[0] > newInterval[1]: # completely after
                last = idx
                afterExists = True
                break
            elif interval[1] < newInterval[0]: # completely before
                ans.append(interval)
            else:
                newInterval[0], newInterval[1] = min(newInterval[0], interval[0]), max(newInterval[1], interval[1])
        
        ans.append(newInterval)
        if afterExists:
            for each in intervals[last:]:
                ans.append(each)

        return ans