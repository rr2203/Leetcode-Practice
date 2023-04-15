#TC: O(1) for both put and get
#SC: O(capacity)

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.head, self.tail = ListNode(None,None),ListNode(None,None)
        self.head.next = self.tail; self.tail.prev = self.head

    def addToStart(self,curNode):
        curNode.next = self.head.next
        curNode.prev = self.head
        self.head.next.prev = curNode
        self.head.next = curNode

    def removeFromLL(self, curNode):
        curNode.next.prev = curNode.prev
        curNode.prev.next = curNode.next

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        curNode = self.mp[key]
        self.removeFromLL(curNode)
        self.addToStart(curNode)
        return curNode.value

    def put(self, key: int, value: int) -> None:
        newNode = self.mp.get(key, None)
        if newNode:
            self.removeFromLL(newNode)
        else:
            newNode = ListNode(key, value)
            self.mp[key] = newNode
        newNode.value = value
        
        self.addToStart(newNode)
        
        if len(self.mp) > self.capacity:
            toBeDeleted = self.tail.prev
            self.mp.pop(toBeDeleted.key)
            self.removeFromLL(toBeDeleted)
            toBeDeleted = None