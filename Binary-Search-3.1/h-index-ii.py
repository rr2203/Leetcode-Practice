#TC: O(lgn)
#SC: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l,r = 0,n-1

        while l<=r:
            mid = (l+r)//2
            if n-mid == citations[mid]:
                return n-mid
            elif citations[mid] < n-mid:
                l = mid+1
            else:
                r = mid-1

        return n-l