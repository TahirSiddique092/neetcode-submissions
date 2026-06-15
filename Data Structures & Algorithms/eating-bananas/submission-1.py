import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = left + ((right - left)//2)
            temp = 0
            for each in piles:
                temp += math.ceil(each/k)
            if temp <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res