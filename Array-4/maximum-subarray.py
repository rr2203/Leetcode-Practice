# TC: O(n) | SC: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum , curSum = -float('inf'), 0
        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            if curSum < 0: curSum = 0
        return maxSum