# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        for i in range(n):
            if p == None:
                return None
            p = p.next
        if p is None:
            return q.next
        while p.next:
            # 双指针
            p = p.next
            q = q.next
        q.next = q.next.next
        return head
