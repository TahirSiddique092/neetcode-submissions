class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(curr, o, c):
            if o == 0 and c == 0:
                result.append(curr)
                return
            if o == 0:
                for _ in range(c):
                    curr += ")"
                result.append(curr)
                return
            if o == c:
                curr += "("
                dfs(curr, o-1, c)
            else:
                curr += "("
                dfs(curr, o-1, c)
                curr = curr[:-1]
                curr += ")"
                dfs(curr, o, c-1)
        
        dfs("", n, n)
        return result
