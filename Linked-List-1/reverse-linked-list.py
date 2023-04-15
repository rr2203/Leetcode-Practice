#Iterative
#TC: O(n)
#SC: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        p,c,n=None,head,head.next
        while c:
            c.next=p
            p=c
            c=n
            if n: n=n.next
        return p

#Recursive
#TC: O(n)
#SC: O(n)
class Solution:
    def reverseList(self, cur_head: Optional[ListNode]) -> Optional[ListNode]:
        if not cur_head or not cur_head.next: return cur_head
        rev_head=self.reverseList(cur_head.next)
        cur_head.next.next=cur_head
        cur_head.next=None
        return rev_head