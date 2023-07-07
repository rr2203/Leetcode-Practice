# TC: O(N) | SC: O(N)
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.ws = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.ws[word].append(i)
        self.d = {}

    @lru_cache(maxsize=None)
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.ws[word1], self.ws[word2]
        i1 = i2 = 0
        dist = float('inf')
        while i1<len(l1) and i2<len(l2):
            dist = min(dist, abs(l2[i2]-l1[i1]))
            if l1[i1] < l2[i2]: i1 += 1
            else:   i2 += 1

        return dist