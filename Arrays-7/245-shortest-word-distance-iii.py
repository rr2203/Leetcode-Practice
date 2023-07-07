# TC: O(N) | SC: O(1)
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dist = len(wordsDict) + 1

        if word1 != word2:
            i1 = i2 = -1
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    if i2!=-1: dist = min(dist, i-i2)
                    i1 = i
                elif wordsDict[i] == word2:
                    if i1!=-1: dist = min(dist, i-i1)
                    i2 = i
        else:
            j = -1
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    if j!=-1: dist = min(dist, i-j)
                    j = i

        return dist