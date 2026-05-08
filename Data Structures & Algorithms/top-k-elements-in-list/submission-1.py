class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for each in nums:
            if each in frequency.keys():
                frequency[each] += 1
            else:
                frequency[each] = 1
        
        counts = [[] for i in range(len(nums)+1)]

        for num, count in frequency.items():
            counts[count].append(num)
        
        result = []
        
        for i in range(len(counts)-1, 0, -1):
            for num in counts[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

        