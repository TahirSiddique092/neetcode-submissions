/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;

        unordered_map<Node*, Node*> clonedMap;

        function<Node*(Node*)> dfs = [&](Node* curr) -> Node* {
            
            if (clonedMap.count(curr)) {
                return clonedMap[curr];
            }

            Node* copy = new Node(curr->val);

            clonedMap[curr] = copy;
            for (Node* neighbor : curr->neighbors) {
                copy->neighbors.push_back(dfs(neighbor));
            }

            return copy;
        };

        return dfs(node);
    }
};
