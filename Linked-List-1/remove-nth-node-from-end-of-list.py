#TC: O(n)
#SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        st,end=head,head
        for i in range(n): 
            end=end.next
            if not end: return head.next
        while end.next: st=st.next; end=end.next
        st.next=st.next.next
        return head
        

        