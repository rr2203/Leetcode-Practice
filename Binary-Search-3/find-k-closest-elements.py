#Two Pointer Solution
#TC: O(n)
#SC: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        i,j = 0, n-1
        while(j-i+1>k):
            if abs(arr[i]-x) <= abs(arr[j]-x):
                j-=1
            else:
                i+=1
        return arr[i:j+1]

#Binary Search Solution 1 - finding closest element to be found and then find the k elements around it
#TC: O(lgn + k)
#SC: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while l<r-1:
            mid = l+(r-l)//2
            if arr[mid] <= x: l = mid
            else: r = mid

        ans = []
        while len(ans) < k and (l>=0 or r<len(arr)):
            if l>=0 and r<len(arr):
                if abs(x-arr[l]) <= abs(x-arr[r]): 
                    ans.append(arr[l])
                    l-=1
                else: 
                    ans.append(arr[r])
                    r+=1
            elif l>=0:
                ans.append(arr[l])
                l-=1
            elif r<len(arr):
                ans.append(arr[r])
                r+=1

        return sorted(ans)

#Binary Search Solution 2 - finding start of final window
#TC: O(lg(n-k) + k)
#SC: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr)-k
        while l<r:
            mid = (l+r)//2
            distS = x - arr[mid]
            distE = arr[mid+k] - x
            if distS > distE:
                l = mid+1
            else:
                r = mid

        return arr[l:l+k]