#TC: O(nlogk)
#SC: O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = [(l.val,i,l) for i,l in enumerate(lists) if l]
        heapq.heapify(minHeap)
        mergedListDummyHead =  ListNode(); tail = mergedListDummyHead
        while minHeap:
            minVal,i,minNode = heapq.heappop(minHeap)
            tail.next = minNode
            tail = minNode
            if minNode.next: heapq.heappush(minHeap, (minNode.next.val, i, minNode.next))
        head = mergedListDummyHead.next; mergedListDummyHead=None
        return head