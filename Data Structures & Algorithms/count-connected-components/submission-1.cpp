class Solution {
private:
    unordered_map<int, vector<int>> adjMap;
    unordered_set<int> visit;
    int count = 0;
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        for(auto edge : edges) {
            adjMap[edge[0]].push_back(edge[1]);
            adjMap[edge[1]].push_back(edge[0]);
        }

        for(int node = 0; node < n; node++) {
            if(!visit.contains(node)) {
                count++;
                dfs(node, -1);
            }
        }

        return count;
    }
private:
    void dfs(int node, int parent) {
        if(visit.contains(node)) return;
        
        visit.insert(node);
        for(int each : adjMap[node]) {
            if(each == parent) continue;
            dfs(each, node);
        }
    }
};
