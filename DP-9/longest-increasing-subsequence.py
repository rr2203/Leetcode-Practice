# Special LIS solution sped up with binary search
# TC: O(nlogn) | SC: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxSub = [nums[0]]

        for num in nums[1:]:
            i = bisect_left(maxSub, num)
            if i == len(maxSub):
                maxSub.append(num)
            else:
                maxSub[i] = num

        return len(maxSub)
    
# General Dynamic Programming Solution
# TC: O(n^2) | SC: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)