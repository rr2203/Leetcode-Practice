#BFS Solution
#TC: O(n*l)
#SC: O(n*l)
from collections import deque
class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = [None]*26

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            child = ord(ch) - ord('a')
            if not cur.children[child]: cur.children[child] = TrieNode()
            cur = cur.children[child]
        cur.word = word

    def findLongestWord(self):
        bfsq = deque()
        bfsq.append(self.root)
        curnode = None
        while bfsq:
            curnode = bfsq.popleft()
            for i in range(25,-1,-1):
                if curnode.children[i] and curnode.children[i].word != "":
                    bfsq.append(curnode.children[i])

        return curnode.word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t  = Trie()
        for w in words: t.insert(w)
        return t.findLongestWord()


#DFS Solution
#TC: O(n*l)
#SC: O(n*l)
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26

class Trie:

    curwordTracker = []

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            child = ord(ch) - ord('a')
            if not cur.children[child]: cur.children[child] = TrieNode()
            cur = cur.children[child]
        cur.isEnd = True
        
    def findLongestWord(self):
        def dfs(curNode):
            maxLevel,maxoutput=0,""
            charsPresent=False
            for i in range(26):
                if curNode.children[i] and curNode.children[i].isEnd :
                    charsPresent=True
                    self.curwordTracker.append(chr(i+ord('a')))
                    nextlevel,output = dfs(curNode.children[i])
                    self.curwordTracker.pop()
                    curlevel = 1 + nextlevel
                    if curlevel>maxLevel:
                        maxLevel=curlevel; maxoutput=copy.deepcopy(output)

            if not charsPresent:
                return 0,copy.deepcopy(self.curwordTracker)
            return maxLevel, maxoutput
            
        return "".join(dfs(self.root)[1])

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t  = Trie()
        for w in words: t.insert(w)
        return t.findLongestWord()