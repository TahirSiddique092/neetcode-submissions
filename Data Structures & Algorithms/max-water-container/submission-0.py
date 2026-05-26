class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        m = 0
        while start < end:
            if m < (end-start) * min(heights[start], heights[end]):
                m = (end-start) * min(heights[start], heights[end])
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return m