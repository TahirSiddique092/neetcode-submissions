class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for each in points:
            d = math.sqrt(each[0]*each[0] + each[1]*each[1])
            heap.append([d, each[0], each[1]])

        heapq.heapify(heap)

        output = []

        for _ in range(k):
            item = heapq.heappop(heap)
            output.append([item[1], item[2]])

        return output