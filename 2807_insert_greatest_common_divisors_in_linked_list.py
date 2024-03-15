# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b = b,(a%b)
            return a
        
        if head.next is None:
            return head
        
        current = head.next
        previous = head
        while current is not None:
            divisor = gcd(previous.val,current.val)
            newnode = ListNode(divisor)
            previous.next = newnode
            newnode.next = current
            
            previous = current
            current = current.next
        
        return head
