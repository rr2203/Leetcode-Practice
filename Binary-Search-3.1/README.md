# Binary-Search-3.1

## Problem1
Optimize Air Routes (https://leetcode.com/discuss/interview-question/1025705/Amazon-or-OA-or-Prime-Air-time/824897) 

There are 3 things to be known before attempting this problem:
maxTravelDist, it is an integer which represents the maximum operating travel distance of the given aircraft;
forwardRouteList, it is a list of pairs of integers where the first integer represents the unique identifier of a forward shipping route and the second integer represents the amount of travel distance required by this shipping route;
returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route
and the second integer represents the amount of travel distance required by this shipping route.

These three things will be given as an input to you. you need to return a list of pairs of integers representing the pairs of IDs of forward and also return the shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.

Example 1:
Input:
maxTravelDist = 7000
forwardRouteList = [[1,2000],[2,4000],[3,6000]]
returnRouteList = [[1,2000]]

Output:
[[2,1]]

Explanation:
There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does not exceed 7000, [2,1] is the optimal pair.


## Problem2
H-Index II (https://leetcode.com/problems/h-index-ii)
