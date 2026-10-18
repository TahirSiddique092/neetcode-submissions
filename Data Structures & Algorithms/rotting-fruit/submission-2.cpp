class Solution {
private:
    int ROWS, COLS, TOT=0;
    set<pair<int, int>> v;
    queue<pair<int, int>> q;

public:
    int orangesRotting(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();
        bool hasFresh = false;

        for(int r = 0; r < ROWS; r++) {
            for(int c = 0; c < COLS; c++) {
                if(grid[r][c] == 2) {
                    q.push({r, c});
                    v.insert({r, c});
                }
                if(grid[r][c] == 1) hasFresh = true;
                if(grid[r][c] != 0) TOT++;
            }
        }

        if(!hasFresh) return 0;

        int min = 0;
        while(q.size() > 0) {
            int layer_size = q.size();
            for(int i = 0; i < layer_size; i++) {
                pair<int, int> p = q.front();
                q.pop();
                addEle(p.first+1, p.second, grid);
                addEle(p.first, p.second+1, grid);
                addEle(p.first-1, p.second, grid);
                addEle(p.first, p.second-1, grid);
            }
            if(!q.empty()) min++;
        }
        if(v.size() == TOT) {
            return min;
        } else {
            return -1;
        }    
    }
private:
    void addEle(int r, int c, vector<vector<int>>& grid) {
        if(r < 0 || r == ROWS || c < 0 || c == COLS || grid[r][c] == 0 || v.contains({r, c})) return;
        q.push({r, c});
        v.insert({r, c});
    }
};
