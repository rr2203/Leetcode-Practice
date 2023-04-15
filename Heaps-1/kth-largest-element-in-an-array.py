# Min Heap based solution
#TC: O(nlogk)
#SC: O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k: heapq.heappop(minHeap)
        return minHeap[0]

# Max Heap based solution
#TC: O(nlog(n-k))
#SC: O(n-k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        n = len(nums)
        ans = float('inf')
        for num in nums:
            heapq.heappush(maxHeap, -num)
            if len(maxHeap) > n-k: 
                ans = min(ans, -heapq.heappop(maxHeap))
        return ans