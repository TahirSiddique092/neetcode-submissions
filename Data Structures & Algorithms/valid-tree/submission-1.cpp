class Solution {
private:
    unordered_set<int> visit;
    unordered_map<int, vector<int>> adjMap;
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if(edges.size() != n - 1) return false;

        for(const auto& edge : edges ) {
            adjMap[edge[0]].push_back(edge[1]);
            adjMap[edge[1]].push_back(edge[0]);
        }

        return dfs(0, -1) && (visit.size() == n);
    }
private:
    bool dfs(int node, int parent) {
        if(visit.contains(node)) return false;

        visit.insert(node);

        for(int neighbour : adjMap[node]) {
            if(neighbour == parent) continue;
            if(!dfs(neighbour, node)) return false;
        }
        
        return true;
    }
};
