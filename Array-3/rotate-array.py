# TC: O(n) | SC: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        def _reverse(s, e):
            nonlocal nums
            while s<e:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1; e-=1

        n = len(nums)
        k %= n
        _reverse(0,n-k-1)
        _reverse(n-k,n-1)
        _reverse(0,n-1)

# TC: O(n) | SC: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]