class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] != "1":
                return
            
            grid[r][c] = "U"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "1":
                    count += 1
                    dfs(r, c)

        return count