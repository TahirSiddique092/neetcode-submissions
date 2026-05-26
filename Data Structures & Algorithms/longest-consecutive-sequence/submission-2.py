class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        start = 0
        end = 0
        longest = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                end += 1
            else:
                if longest < end - start + 1:
                    longest = end - start + 1
                start = end

        if longest < end - start + 1:
            longest = end - start + 1

        return longest
            