# Constant space DP solution
# TC: O(n) | SC: O(1)
class Solution:
    def numberOfArithmeticSlices(self, A):
        dp = 0
        sum_ = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp = 1 + dp
                sum_ += dp
            else:
                dp = 0
        return sum_

# Math solution
# TC: O(n) | SC: O(1)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0

        curDiff = nums[1]-nums[0]
        windowSize = 2
        ans = 0
        calculateNumOfPartitions = lambda k: (k+1)*(k-2) - (k*(k+1)//2 - 3)

        for i in range(2,n):
            if nums[i] - nums[i-1] == curDiff:
                windowSize += 1
            else:
                if windowSize >= 3: ans += calculateNumOfPartitions(windowSize)
                windowSize = 2
                curDiff = nums[i] - nums[i-1]

        if windowSize >= 3: ans += calculateNumOfPartitions(windowSize)

        return ans