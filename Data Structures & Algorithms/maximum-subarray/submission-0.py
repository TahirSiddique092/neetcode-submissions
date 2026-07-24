class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxSubArray(self, nums: List[int]) -> int:
        preSum = 0
        for num in nums:
            if (preSum + num) > num:
                preSum += num
            else:
                preSum = num
            self.maxSum = max(self.maxSum, preSum)
        return self.maxSum