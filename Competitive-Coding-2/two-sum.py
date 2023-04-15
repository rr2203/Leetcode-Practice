#TC: O(n)
#SC: O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_map=dict()
        for i,num in enumerate(nums):
            if target-num in nums_index_map:
                return nums_index_map[target-num],i
            else:
                nums_index_map[num]=i
        return -1

#TC: O(nlogn)
#SC: O(1)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index=[]
        for i in range(len(nums)): num_index.append((nums[i],i))
        num_index.sort()
        i,j=0,len(num_index)-1
        while i<j:
            if num_index[i][0]+num_index[j][0]==target:
                return num_index[i][1],num_index[j][1]
            elif num_index[i][0]+num_index[j][0]<target:
                i+=1
            else:
                j-=1
        return -1

