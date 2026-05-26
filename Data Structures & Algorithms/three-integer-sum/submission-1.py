class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for idx, ele in enumerate(nums):
            target = -1 * ele
            i = idx+1
            j = len(nums)-1
            while i < j:
                if (nums[i] + nums[j] == target and [ele, nums[i], nums[j]] not in result):
                    result.append([ele, nums[i], nums[j]])
                if nums[i]+nums[j] < target:
                    i = i+1
                else:
                    j = j-1
        return result
                
