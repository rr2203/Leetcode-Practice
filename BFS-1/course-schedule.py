#TC :O(n)
#SC: O(n)
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees=[0]*numCourses
        adjacency_list=[[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjacency_list[prereq[1]].append(prereq[0])
            indegrees[prereq[0]]+=1
        
        bfsq = collections.deque()
        for i in range(numCourses):
            if indegrees[i]==0: bfsq.append(i)
        while bfsq:
            cur_node=bfsq.popleft()
            for neighbour in adjacency_list[cur_node]:
                if indegrees[neighbour]>0:
                    indegrees[neighbour]-=1
                    if indegrees[neighbour]==0:
                        bfsq.append(neighbour)

        return indegrees.count(0)==len(indegrees)
        