# TC: O(N) | SC: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        
        for num, count in Counter(nums).items():
            buckets[count].append(num)

        ans = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
                k-=1
                if k == 0: return ans

        return ans

# TC: O(nlogk) | SC: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        minHeap = []
        for num, count in counts.items():
            if len(minHeap) < k: heapq.heappush(minHeap, (count, num))
            else:
                prevCount, prevNum = minHeap[0]
                if prevCount < count:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (count, num))

        return [key for val,key in minHeap]