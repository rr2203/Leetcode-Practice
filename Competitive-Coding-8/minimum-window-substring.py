#TC: O(s)
#SC: O(1)

from collections import defaultdict
class Solution:

    def isTargetPresent(self, tf, cf):
        isTargetPresent = True
        for key,freq in tf.items():
            if cf.get(key,0) < freq: 
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        cf,tf = defaultdict(int), defaultdict(int)
        for c in t: tf[c]+=1

        minLen = float('inf')
        besti,bestj=-1,-1
        i=0
        for j,c in enumerate(s):
            cf[c]+=1

            #minimize window
            while i<=j and self.isTargetPresent(tf, cf):
                if j-i+1 < minLen:
                    minLen = j-i+1
                    besti,bestj=i,j
                cf[s[i]]-=1
                if cf[s[i]] == 0:
                    cf.pop(s[i])
                i+=1

        return s[besti:bestj+1]