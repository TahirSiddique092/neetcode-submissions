class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for each in points:
            d = each[0]*each[0] + each[1]*each[1]
            heap.append([d, each])

        heapq.heapify(heap)

        output = []

        for _ in range(k):
            item = heapq.heappop(heap)
            output.append(item[1])

        return output