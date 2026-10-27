class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if(wordList.end() == find(wordList.begin(), wordList.end(), endWord)) return 0;

        unordered_map<string, vector<string>> neighbours;
        unordered_set<string> visit;
        queue<string> q;
        int result = 1;

        wordList.push_back(beginWord);

        for(string word : wordList) {
            for(int i = 0; i < word.size(); i++) {
                string pattern = word.substr(0, i) + "*" + word.substr(i + 1);
                neighbours[pattern].push_back(word);
            }
        }

        q.push(beginWord);
        visit.insert(beginWord);

        while(q.size() != 0) {
            int curr_size = q.size();
            for(int i = 0; i < curr_size; i++) {
                string word = q.front();
                q.pop();
                if(word == endWord) return result;

                for(int j = 0; j < word.size(); j++) {
                    string pattern = word.substr(0, j) + "*" + word.substr(j + 1);
                    for(string n : neighbours[pattern]) {
                        if(!visit.contains(n)) {
                            visit.insert(n);
                            q.push(n);
                        }
                    }
                }
            }
            result++;
        }
        return 0;
    }
};
