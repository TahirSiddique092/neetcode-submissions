class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        output = []
        while r < len(nums):
            output.append(max(nums[l:r+1]))
            l += 1
            r += 1
        return output