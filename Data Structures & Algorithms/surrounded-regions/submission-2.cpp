class Solution {
private:
    set<pair<int, int>> visit;
    int ROWS, COLS;

public:
    void solve(vector<vector<char>>& board) {
        ROWS = board.size();
        COLS = board[0].size();

        for(int r = 0; r < ROWS; r++) {
            dfs(r, 0, board);
            dfs(r, COLS - 1, board);
        }

        for(int c = 0; c < COLS; c++) {
            dfs(0, c, board);
            dfs(ROWS - 1, c, board);
        }

        for(int r = 0; r < ROWS; r++) {
            for(int c = 0; c < COLS; c++) {
                if(board[r][c] == 'O' && !visit.contains({r, c})) {
                    board[r][c] = 'X';
                }
            }
        }
    }

private:
    void dfs(int r, int c, vector<vector<char>>& board) {
        if(r == ROWS || r < 0 || c == COLS || c < 0 || board[r][c] == 'X' || visit.contains({r, c})) return;
        visit.insert({r, c});

        dfs(r + 1, c, board);
        dfs(r - 1, c, board);
        dfs(r, c + 1, board);
        dfs(r, c - 1, board);
    }
};
