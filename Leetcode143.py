# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        p = slow.next # 后半段给p
        right = None
        slow.next = None
        while p:
            right,right.next, p = p,right,p.next # 翻转后半段
        # 重排链表
        left = head
        while left and right:
            left.next,right.next,left,right = right,left.next,left.next,right.next
        
