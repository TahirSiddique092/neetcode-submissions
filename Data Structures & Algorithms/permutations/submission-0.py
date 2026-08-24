class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(curr, rem):
            if not rem:
                result.append(curr.copy())
                return
            
            for i in rem:
                newCurr = curr.copy()
                newCurr.append(i)
                newRem = rem.copy()
                newRem.remove(i)
                dfs(newCurr, newRem)
    
        dfs([], nums)
        return result