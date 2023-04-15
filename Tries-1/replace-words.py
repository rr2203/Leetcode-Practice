#TC: O(m*l + n*k)
#SC: O(m*l + n*k)

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26

class Trie:

    curWordTracker = []

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            childIndex = ord(c) - ord('a')
            if not cur.children[childIndex]: cur.children[childIndex] = TrieNode()
            cur = cur.children[childIndex]
        cur.isEnd = True

    def findRoot(self, word):
        self.curWordTracker.clear()
        cur = self.root
        for c in word:
            childIndex = ord(c) - ord('a')
            if not cur.children[childIndex]: return None
            self.curWordTracker.append(c)
            cur = cur.children[childIndex]
            if cur.isEnd: break
                
        rootWord = "".join(self.curWordTracker)
        return rootWord

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for word in dictionary: t.insert(word)

        sentenceWords = sentence.split(" ")
        ans = []
        for i,word in enumerate(sentenceWords):
            rootword = t.findRoot(word)
            if rootword: sentenceWords[i] = rootword
            ans.append(sentenceWords[i]); ans.append(" ")
            
        return "".join(ans)[:-1]
