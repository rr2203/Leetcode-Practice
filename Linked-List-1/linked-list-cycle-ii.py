#TC: O(n)
#SC: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        slow,fast=head,head
        has_cycle=False
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow==fast: has_cycle=True; break
        if not has_cycle: 
            return None

        slow=head
        while(slow!=fast): slow=slow.next; fast=fast.next

        return slow