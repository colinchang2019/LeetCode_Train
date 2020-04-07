# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        xmin = ListNode(0)
        xmax = ListNode(1)
        r1,r2 = xmin,xmax
        while head is not None:
            if head.val<x:
                r1.next = head
                r1 = r1.next
            else:
                r2.next = head
                r2 = r2.next
            head = head.next
        r2.next = None
        r1.next = xmax.next
        return xmin.next
