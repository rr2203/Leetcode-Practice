# TC: O(n) | SC: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxReach = 0
        for i in range(n):
            if i>maxReach: break
            maxReach = max(maxReach, i+nums[i])
            if maxReach >= n-1: return True
        return False