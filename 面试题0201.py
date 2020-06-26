# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        d = set([head.val])
        h,r = head,head.next
        while r:
            if r.val in d:
                r = r.next
                continue
            d.add(r.val)
            h.next = r
            h,r = h.next,r.next
        h.next = None
        return head
