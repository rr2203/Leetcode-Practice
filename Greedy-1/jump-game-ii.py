# TC: O(n) | SC: O(1)
class Solution:
    def jump(self, nums):
        if len(nums) <= 1:  return 0

        curmax = nums[0]
        nextmax = nums[0]
        jumps = 1

        for i in range(1, len(nums)):
            nextmax = max(i + nums[i], nextmax)

            if curmax == i and i != len(nums) - 1:
                curmax = nextmax
                jumps += 1

            if curmax >= len(nums) - 1:
                break

        return jumps