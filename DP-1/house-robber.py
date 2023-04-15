#TC: O(n)
#SC: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevprev,prev=0,nums[0]
        for i in range(1,len(nums)):
            temp=prev
            prev=max(prev, nums[i]+prevprev)
            prevprev=temp

        return max(prev,prevprev)