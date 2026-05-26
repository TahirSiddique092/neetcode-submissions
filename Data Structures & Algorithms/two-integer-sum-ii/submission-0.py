class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, ele in enumerate(numbers):
            if target-ele in numbers[idx+1:]:
                return [idx+1, numbers.index(target-ele)+1]