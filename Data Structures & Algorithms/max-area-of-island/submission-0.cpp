class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        size_t ROWS = grid.size();
        size_t COLS = grid[0].size();
        int result = 0;

        function<int(int, int)> dfs = [&](int r, int c) -> int {
            if ((r >= ROWS) || (r < 0) ||
                (c >= COLS) || (c < 0) || 
                (grid[r][c] != 1)
            ) return 0;

            grid[r][c] = -1;

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1);
        };

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    result = max(result, dfs(r, c));
                };
            };
        };

        return result;
    }
};
