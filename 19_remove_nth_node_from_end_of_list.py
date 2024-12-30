# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        pnt1 = head
        pnt2 = head.next
        for i in range(n-1):
            if pnt2.next == None:
                head = head.next
                return head
            else:
                pnt2 = pnt2.next
        while(pnt2.next):
            pnt1 = pnt1.next
            pnt2 = pnt2.next
        pnt1.next = pnt1.next.next
        return head
