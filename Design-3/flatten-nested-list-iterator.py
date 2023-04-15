#TC: O(n)
#SC: O(depth of nested lists)

class NestedIterator():
    def __init__(self, nestedList: [NestedInteger]):
        self.st = [iter(nestedList)]
        self.nextElement = None
    
    def next(self) -> int:
        return self.nextElement
    
    def hasNext(self) -> bool:
        st = self.st
        while st:
            self.nextElement = next(st[-1], None)
            if self.nextElement:
                if self.nextElement.isInteger(): return True
                else: st.append(iter(self.nextElement.getList()))
            else:
                st.pop()
        return False