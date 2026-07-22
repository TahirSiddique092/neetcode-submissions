class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 1
        intervals.sort()
        temp = intervals[0]
        while i < len(intervals):
            if not temp[1] >= intervals[i][0]:
                ans.append(temp)
                temp = intervals[i]
            else:
                temp = [min(temp[0], intervals[i][0]), max(temp[1], intervals[i][1])]
            i += 1
        
        ans.append(temp)

        return ans