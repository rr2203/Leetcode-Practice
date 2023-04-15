"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

#TC: O(n)
#SC: O(n)
def dfs(id,mp):
    e=mp[id]
    imp, children = e.importance,e.subordinates
    for c in children:
        imp += dfs(c,mp)
    return imp

class Solution:
    def getImportance(self, employees: List['Employee'], eid: int) -> int:
        mp={}
        for e in employees:
            mp[e.id]=e
        return dfs(eid,mp)