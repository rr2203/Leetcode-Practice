# TC: O(n) | SC: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        i = n-1
        while i>=1 and nums[i-1] >= nums[i]:    i -= 1

        if i!= 0:
            j = n-1
            while nums[j] <= nums[i-1] : j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        
        st,end = i,n-1
        while st <= end:
           nums[st], nums[end] = nums[end], nums[st] 
           st+=1; end-=1
        