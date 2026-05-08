class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, ele in enumerate(nums) :
            second = target - ele
            if second in nums[i+1:] :
                result.append(i)
                idx = nums[i+1:].index(second) + i + 1
                result.append(idx)
                return result
        