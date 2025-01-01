# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow = head
        prev = None
        fast = head
        while(slow,fast):
            if fast.next == None:
                prev.next = slow.next
                return head
            if fast.next.next == None:
                slow.next = slow.next.next
                return head
            prev = slow
            slow = slow.next
            fast = fast.next.next
