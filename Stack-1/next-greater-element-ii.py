# TC: O(n) | SC: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        circNums = nums + nums
        stack = []
        n = len(nums)
        ans = [-1] * (2*n)

        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= circNums[i]: stack.pop()
            if stack:   ans[i] = stack[-1]
            stack.append(circNums[i])

        return ans[:n]