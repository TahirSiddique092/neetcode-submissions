class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        # here code means coding the nxn grid into a list of n numbers
        # initially code = [-1,-1,...n-1 times]

        def valid_positions(code, i):
            # TODO this should return an array which has valid 
            # positions for the placement of queen in ith row
            valid = [x for x in range(n)]
            for k in range(i):
                if code[k] in valid: 
                    valid.remove(code[k])

                right_hor = code[k] + (i - k)
                if right_hor < n and right_hor in valid:
                    valid.remove(right_hor)
                
                left_hor = code[k] - (i - k)
                if left_hor >= 0 and left_hor in valid:
                    valid.remove(left_hor)

            return valid

        def dfs(code, i):
            if i == n:
                temp = ["."*n for _ in range(n)]
                for idx in range(n):
                    t_str = temp[idx]
                    t_str = t_str[:code[idx]] + "Q" + t_str[code[idx]+1:]
                    temp[idx] = t_str
                result.append(temp.copy())
                return

            positions = valid_positions(code, i)

            for pos in positions:
                new_code = code.copy()
                new_code[i] = pos
                dfs(new_code, i+1)
        
        dfs([-1 for _ in range(n)], 0)
        return result