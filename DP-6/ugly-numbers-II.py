# TC: O(n) | SC: O(n)
class Solution:
    def nthUglyNumber(self, n):
        p2 = p3 = p5 = 0
        n2,n3,n5 = 2,3,5
        arr = [0] * n
        arr[0] = 1

        for i in range(1, n):
            min_val = min(n2, n3, n5)
            arr[i] = min_val

            if min_val == n2:
                p2 += 1
                n2 = 2 * arr[p2]

            if min_val == n3:
                p3 += 1
                n3 = 3 * arr[p3]

            if min_val == n5:
                p5 += 1
                n5 = 5 * arr[p5]

        return arr[-1]

# TC: O(nlogn) | SC: O(n)
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        set_ = set()
        pq = []
        i = 0
        curUglyNum = 1
        heapq.heappush(pq, curUglyNum)
        set_.add(curUglyNum)
        primes = [2, 3, 5]
        while i < n:
            curUglyNum = heapq.heappop(pq)
            for prime in primes:
                newUglyNum = prime * curUglyNum
                if newUglyNum not in set_:
                    set_.add(newUglyNum)
                    heapq.heappush(pq, newUglyNum)
            i += 1
        return curUglyNum