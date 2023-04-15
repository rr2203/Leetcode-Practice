#TC: 
# insert : O(l)
# search: O(l)
# startsWith: O(l)

#SC: 
# Trie: O(n*l)

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            child=ord(c)-ord('a')
            if cur.children[child] == None: cur.children[child] = TrieNode()
            cur = cur.children[child]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            child=ord(c)-ord('a')
            if cur.children[child] == None: return False
            cur = cur.children[child]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            child=ord(c)-ord('a')
            if cur.children[child] == None: return False
            cur = cur.children[child]
        return True