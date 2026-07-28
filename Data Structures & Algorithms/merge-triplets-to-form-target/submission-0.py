class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # remove which are big than target.
        for i in range(3):
            for idx, each in enumerate(triplets):
                if each[i] > target[i]:
                    triplets.pop(idx)

        # check if all the three exists in any of the triplets. 
        for i in range(3):
            exists = False
            for each in triplets:
                if each[i] == target[i]:
                    exists = True
            if not exists:
                return False

        return True