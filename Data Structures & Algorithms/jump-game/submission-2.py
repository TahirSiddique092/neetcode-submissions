class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        i = 0
        while i < len(nums) and i <= furthest:
            furthest = max(furthest, i + nums[i])
            if furthest >= len(nums)-1:
                return True
            i += 1
        return False