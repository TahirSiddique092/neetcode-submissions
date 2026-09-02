class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(curr, i):
            if i >= len(nums):
                if curr not in result:
                    result.append(curr.copy())
                return
            # include ith num
            curr.append(nums[i])
            dfs(curr, i+1)
            # exclude ith num and all occurences
            curr.pop()
            dfs(curr, len(nums) - nums[::-1].index(nums[i]))

        dfs([], 0) 
        return result