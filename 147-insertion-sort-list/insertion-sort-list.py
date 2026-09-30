class Solution:
    def insertionSortList(self,head:Optional[ListNode])->Optional[ListNode]:
        a=ListNode(0)

        while head:
            x=a

            while x.next and x.next.val<head.val:
                x=x.next

            y=head.next
            head.next=x.next
            x.next=head
            head=y

        return a.next