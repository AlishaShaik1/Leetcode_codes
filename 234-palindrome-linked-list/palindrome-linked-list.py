# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        if fast:
            slow=slow.next

        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        p1=head
        p2=prev

        while p2:
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True
        
        
        
