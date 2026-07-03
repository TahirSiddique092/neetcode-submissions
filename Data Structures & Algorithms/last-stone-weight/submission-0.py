class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x, y = stones.pop(), stones.pop()

            if x > y:
                stones.append(x-y)
                
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
