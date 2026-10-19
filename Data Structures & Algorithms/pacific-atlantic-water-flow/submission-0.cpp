class Solution {
private:
    set<pair<int, int>> pac, atl;
    vector<vector<int>> result;
    int ROWS, COLS;

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        ROWS = heights.size();
        COLS = heights[0].size();

        for(int r = 0; r < ROWS; r++) {
            dfs(r, 0, heights[r][0], heights, pac);
            dfs(r, COLS-1, heights[r][COLS-1], heights, atl);
        }

        for(int c = 0; c < COLS; c++) {
            dfs(0, c, heights[0][c], heights, pac);
            dfs(ROWS-1, c, heights[ROWS-1][c], heights, atl);
        }   

        for(int r = 0; r < ROWS; r++) {
            for(int c = 0; c < COLS; c++) {
                if(pac.contains({r, c}) && atl.contains({r, c})) {
                    result.push_back({r, c});
                }
            }
        }
        return result; 
    }

private:
    void dfs(int r, int c, int prevHeight, vector<vector<int>>& heights, set<pair<int, int>>& visit) {
        if(r < 0 || c < 0 || r == ROWS || c == COLS || heights[r][c] < prevHeight) return;
        
        if(visit.contains({r, c})) return;

        visit.insert({r, c});
        
        dfs(r + 1, c, heights[r][c], heights, visit);
        dfs(r - 1, c, heights[r][c], heights, visit);
        dfs(r, c + 1, heights[r][c], heights, visit);
        dfs(r, c - 1, heights[r][c], heights, visit);
    }
};
