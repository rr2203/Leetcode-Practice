# TC: O(n) | SC: O(1)
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = sorted(Counter(tasks).values())
        maxVal = counts[-1] - 1
        idleSlots = maxVal * n

        for i in range(len(counts)-2, -1, -1):
            idleSlots -= min(counts[i], maxVal)
        
        return len(tasks) + idleSlots if idleSlots > 0 else len(tasks)

# Heap based solution
# TC: O(n) | SC: O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        underCoolDown = deque()
        time = 0
        while maxHeap or underCoolDown:
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    underCoolDown.append((freq , time+n+1))

            time += 1
            if underCoolDown and underCoolDown[0][1] == time :
                    heapq.heappush(maxHeap, underCoolDown.popleft()[0])

        return time