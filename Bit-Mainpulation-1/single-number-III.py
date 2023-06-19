# TC: O(n) | SC: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor1 = 0
        for num in nums: xor1 ^= num

        temp = xor1 & (-xor1)
        xor2 = 0
        for num in nums:
            if (temp & num) != 0:   xor2 ^= num

        return [xor2, xor1 ^ xor2]