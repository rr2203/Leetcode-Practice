# TC : O(n)
# SC: O(1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stmap = dict();  tset = set()
        for si, ti in zip(s, t):
            if si not in stmap and ti not in tset:
                    stmap[si] = ti;   tset.add(ti)
            elif stmap.get(si) != ti or (si not in stmap and ti in tset):
                return False

        return True