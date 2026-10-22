class Solution {
private:
    map<int, vector<int>> preq;
    set<int> visit, cycle;
    vector<int> output; 
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for(int i = 0; i < numCourses; i++) {
            preq[i] = {};
        }

        for(int i = 0; i < prerequisites.size(); i++) {
           preq[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        for(int i = 0; i < numCourses; i++) {
            if(!dfs(i)) return {};
        }

        return output;
    }
private:
    bool dfs(int course) {
        if(cycle.contains(course)) return false;
        if(visit.contains(course)) return true;

        cycle.insert(course);
        for(int i = 0; i < preq[course].size(); i++) {
            if(!dfs(preq[course][i])) return false;
        }
        cycle.erase(course);
        visit.insert(course);
        output.push_back(course);
        return true;
    }
};
