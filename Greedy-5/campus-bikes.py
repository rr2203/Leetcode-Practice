# TC: O(m*n) | SC: O(m*n)
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        manhattan = lambda x,y: (abs(x[0]-y[0]) + abs(x[1]-y[1]))
        distances = [[] for _ in range(2000)]
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = manhattan(workers[i], bikes[j])
                distances[dist].append((i, j))

        ans = [-1] * len(workers)
        bikeSet = set()
        for distList in distances:
            for workerID, bikeID in distList:
                if ans[workerID] == -1 and bikeID not in bikeSet:
                    ans[workerID] = bikeID
                    bikeSet.add(bikeID)

        return ans

# TC: O(m*n*log(m*n)) | SC: O(m*n)
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        manhattan = lambda x,y: (abs(x[0]-y[0]) + abs(x[1]-y[1]))
        arr = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = manhattan(workers[i], bikes[j])
                arr.append((dist, i, j))

        arr.sort()

        ans = [-1] * len(workers)
        bikeSet = set()
        for dist, workerID, bikeID in arr:
            if ans[workerID] == -1 and bikeID not in bikeSet:
                ans[workerID] = bikeID
                bikeSet.add(bikeID)

        return ans