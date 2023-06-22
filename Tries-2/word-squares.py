# TC: O(N * 4^N) | SC: O(N)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.startsWith = []

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node.startsWith.append(word)
            node = node.children[c]

    def searchPrefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return []
            node = node.children[c]
        return node.startsWith

class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        result = []
        trie = Trie()
        for word in words: trie.insert(word)

        curWordSqureList = []
        def backtrack(k):
            nonlocal curWordSqureList, result

            if len(curWordSqureList) == k:  
                result.append(curWordSqureList[:])
                return

            prefix = ""
            for word in curWordSqureList:   prefix += word[len(curWordSqureList)]

            possibleWords = trie.searchPrefix(prefix)
            for word in possibleWords:
                curWordSqureList.append(word)
                backtrack(k)
                curWordSqureList.pop()

        for word in words:
            curWordSqureList.append(word)
            backtrack(len(word))
            curWordSqureList.pop()

        return result