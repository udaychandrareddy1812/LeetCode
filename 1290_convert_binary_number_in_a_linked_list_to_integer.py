# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''
        pointer = head.next
        while pointer:
            binary = binary + str(pointer.val)
            pointer = pointer.next
        binary = str(head.val) + binary
        decimal = int(binary, 2)
        return decimal
