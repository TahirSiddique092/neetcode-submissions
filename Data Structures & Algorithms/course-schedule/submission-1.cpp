class Solution {
private:
    unordered_map<int, set<int>> dict;

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for(int i = 0; i < numCourses; i++) {
            dict[i] = {};
        }

        for(auto each : prerequisites) {
            dict[each[0]].insert(each[1]);
        }

        for(int i = 0; i < numCourses; i++) {
            set<int> temp;
            if(!graph(i, temp)) return false; 
        }

        return true;
    }

private:
    bool graph(int course, set<int>& visit) {
        if(visit.contains(course)) return false;
        if(dict[course].empty()) return true;

        visit.insert(course);

        for(int each : dict[course]) {
            if(!graph(each, visit)) return false;
        }

        visit.erase(course);
        dict[course].clear();
        
        return true;
    }
};
