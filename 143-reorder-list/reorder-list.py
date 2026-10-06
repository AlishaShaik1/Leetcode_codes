class Solution:
    def reorderList(self,head:Optional[ListNode])->None:
        if not head or not head.next:
            return

        a=head
        b=head

        while b and b.next:
            a=a.next
            b=b.next.next

        c=a.next
        a.next=None

        a=None
        while c:
            b=c.next
            c.next=a
            a=c
            c=b

        b=head
        while a:
            c=b.next
            d=a.next
            b.next=a
            a.next=c
            b=c
            a=d