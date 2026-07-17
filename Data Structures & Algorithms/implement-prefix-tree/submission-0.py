class Node:
    def __init__(self, data = "", end = False):
        self.data = data
        self.end = end
        self.conn = [None for _ in range(26)]

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        tmp = self.head
        for i in range(len(word)):
            if not tmp.conn[ord(word[i])-ord('a')]:
                node = Node(word[i])
                tmp.conn[ord(word[i])-ord('a')] = node
            tmp = tmp.conn[ord(word[i])-ord('a')] 
        tmp.end = True

    def search(self, word: str) -> bool:
        tmp = self.head
        for i in range(len(word)):
            if not tmp.conn[ord(word[i])-ord('a')]:
                return False
            tmp = tmp.conn[ord(word[i])-ord('a')]
        if tmp.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        tmp = self.head
        for i in range(len(prefix)):
            if not tmp.conn[ord(prefix[i])-ord('a')]:
                return False
            tmp = tmp.conn[ord(prefix[i])-ord('a')]
        return True
        
        