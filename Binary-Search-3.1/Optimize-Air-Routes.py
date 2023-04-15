# assuming sorted arrays, no repetition of distances, non empty arrays

# two pointer solution
#TC: O(m+n)
#SC: O(1)
def solution1(forwardRouteList, returnRouteList, maxTravelDist):
    m,n = len(forwardRouteList), len(returnRouteList)
    l,r = 0, n-1
    ans = []
    curMax = 0
    while l<m and r>=0:
        dist = forwardRouteList[l][1] + returnRouteList[r][1]

        if dist <= maxTravelDist:
            if dist == curMax:
                ans.append(forwardRouteList[l][0], returnRouteList[r][0])
            elif dist > curMax:
                curMax = dist
                ans = [[forwardRouteList[l][0], returnRouteList[r][0]]]
        
        if dist < maxTravelDist:
            l+=1
        elif dist > maxTravelDist:
            r-=1
        else:
            l+=1; r-=1

    return ans

print(solution1([[1,2000],[2,4000],[3,6000]], [[1,2000]], 7000))

# binary search
#TC: O(min(m,n) lg(max(m,n)))
#SC: O(1)
def solution2(forwardRouteList, returnRouteList, maxTravelDist):
    m,n = len(forwardRouteList), len(returnRouteList)
    x,y = forwardRouteList, returnRouteList
    reversedLists = False
    if m>n: 
        x,y = y,x; reversedLists = True

    ans = []
    curMax = 0
    for xid, xdist in x:
        remainingDist = maxTravelDist - xdist
        l,r = 0, len(y)-1
        while l<r-1:
            mid = (l+r)//2
            if remainingDist > y[mid][1]:
                l = mid
            else:
                r = mid-1
        dist = xdist + y[l][1]
        if dist <= maxTravelDist:
            if dist == curMax:
                ans.append(xid, y[l][0])
            elif dist > curMax:
                curMax = dist
                ans = [[xid, y[l][0]]]

    if reversedLists:
        for i in range(len(ans)): ans[i][0],ans[i][1] = ans[i][1],ans[i][0]

    return ans

print(solution2([[1,2000],[2,4000],[3,6000]], [[1,2000]], 7000))