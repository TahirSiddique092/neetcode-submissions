class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)
            
        return abs(stones[0]) if len(stones) == 1 else 0
