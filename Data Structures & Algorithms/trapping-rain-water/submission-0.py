class Solution:
    def trap(self, height: List[int]) -> int:
        water = []
        for i in range(1,len(height)-1):
            l = max(height[:i])
            r = max(height[i+1:])
            m = min(l,r)
            m -= height[i]
            water.append(m if m >= 0 else 0)
        return sum(water)
