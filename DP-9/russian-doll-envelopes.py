# TC: O(nlogn) | SC: O(n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))

        def lis(nums):
            n = len(nums)
            if n<1: return 0
            maxSub = [nums[0]]
            for num in nums[1:]:
                i = bisect_left(maxSub, num)
                if i == len(maxSub):    maxSub.append(num)
                else: maxSub[i] = num

            return len(maxSub)

        return lis([x[1] for x in envelopes])