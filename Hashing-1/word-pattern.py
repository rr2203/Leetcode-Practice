# TC : O(n)
# SC: O(1)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split(' ')
        if len(pattern) != len(s_words): return False

        pattern_s_map = dict();   s_set = set()
        for pattern_i, s_i in zip(pattern, s_words):
            if pattern_i not in pattern_s_map and s_i not in s_set:
                pattern_s_map[pattern_i] = s_i;   s_set.add(s_i)
            elif pattern_s_map.get(pattern_i) != s_i or (pattern_i not in pattern_s_map and s_i in s_set):
                return False

        return True
