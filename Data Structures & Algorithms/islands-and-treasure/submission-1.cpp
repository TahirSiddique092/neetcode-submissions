class Solution {
private:
    set<pair<int, int>> v;
    queue<pair<int, int>> q;
    int ROWS, COLS;

public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();

        for(int r = 0; r < ROWS; r++) {
            for(int c = 0; c < COLS; c++) {
                if(grid[r][c] == 0) {
                    q.push({r, c});
                    v.insert({r, c});
                }
            }
        }

        int dist = 0;
        
        while(q.size() > 0) {
            int layer_size = q.size();
            for(int i = 0; i < layer_size; i++) {
                pair<int, int> p = q.front();
                q.pop();
                grid[p.first][p.second] = dist;
                addEle(p.first, p.second+1, grid);
                addEle(p.first+1, p.second, grid);
                addEle(p.first, p.second-1, grid);
                addEle(p.first-1, p.second, grid);
            }
            dist++;
        }
    }
private:
    void addEle(int r, int c, vector<vector<int>>& grid) {
        if(r < 0 || r == ROWS || c < 0 || c == COLS || grid[r][c] == -1 || v.contains({r, c})) return;
        q.push({r, c});
        v.insert({r, c});
    }
};
