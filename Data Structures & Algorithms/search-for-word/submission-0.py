class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        column = len(board[0])
        target = len(word)
        
        def dfs(i, j, k):
            if k == target:
                return True

            if i < 0 or i >= row or j < 0 or j >= column or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"

            found = (
                dfs(i, j+1, k+1) or 
                dfs(i, j-1, k+1) or 
                dfs(i+1, j, k+1) or 
                dfs(i-1, j, k+1)
            )

            board[i][j] = temp
            
            return found


        for i in range(row):
            for j in range(column):
                if dfs(i, j, 0):
                    return True

        return False   