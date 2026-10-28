class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        unordered_set<int> visit;
        unordered_map<int, vector<pair<int, int>>> adjMap;

        for(auto edge : times) {
            adjMap[edge[0]].push_back({edge[2], edge[1]});
        }

        minHeap.push({0, k});

        int time = 0;
        while(minHeap.size() > 0) {
            if(visit.size() == n) break;
            auto node = minHeap.top();
            minHeap.pop();

            if(visit.contains(node.second)) continue; 
            
            visit.insert(node.second);

            time = node.first;

            for(auto neighbour : adjMap[node.second]) {
                minHeap.push({node.first + neighbour.first, neighbour.second});
            }

        }

        if(visit.size() == n) return time;
        else return -1;
    }
};
