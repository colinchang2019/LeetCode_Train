# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast,slow,pre = head,head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        while pre.next!=slow:
            pre = pre.next
        p = TreeNode(slow.val)
        pre.next = None
        pre.next,hright = None,slow.next
        p.left = self.sortedListToBST(head)
        p.right = self.sortedListToBST(hright)
        return p
