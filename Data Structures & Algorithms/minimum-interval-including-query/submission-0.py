class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []

        for q in queries:
            l = float('inf')
            for i in intervals:
                if q >= i[0] and q <= i[1] and l > (i[1]-i[0]+1):
                    l = i[1]-i[0]+1
            output.append(l if l != float('inf') else -1)
        return output