class Node:
    def __init__(self, data="", end=False):
        self.data = data
        self.end = end
        self.conn = dict()

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if not curr.conn.get(char, None):
                curr.conn[char] = Node(char)
            curr = curr.conn[char]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):

            if i == len(word):
                return node.end

            if word[i] != '.':
                if word[i] not in node.conn:
                    return False
                return dfs(node.conn[word[i]], i + 1)

            for child in node.conn.values():
                if dfs(child, i + 1):
                    return True

            return False

        return dfs(self.head, 0)
                

