#TC: O(n)
#SC: O(1)
class Solution:

    def rev(self,head):
        p,c,n=None,head,head.next
        while c:
            c.next=p
            p=c 
            c=n
            if n: n=n.next
        return p

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True

        #find mid
        s,f=head,head
        while f.next and f.next.next:
            s=s.next; f=f.next.next
        #rev second part
        head2=self.rev(s.next)

        #break the two lists and check if equal/1 diff
        s.next=None
        s,f=head,head2
        while s and f:
            if s.val!=f.val: return False
            s=s.next; f=f.next
        
        return True