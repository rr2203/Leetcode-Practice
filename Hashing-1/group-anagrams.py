# TC: O(nk)
# SC: O(1)
from collections import defaultdict

def hashValue(s) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ,101, 103]
    result = 1
    for c in s: result *= primes[ord(c) - ord('a')]
    return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_strlist_map = defaultdict(list)
        for s in strs:
            freq_strlist_map[hashValue(s)].append(s)

        ans = []
        for strs in freq_strlist_map.values():
            ans.append(strs)
        return ans
