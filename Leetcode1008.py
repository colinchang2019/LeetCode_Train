# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        for i in range(len(preorder)):
            if i<len(preorder) and preorder[i]>preorder[0]:
                break
        if preorder[i]<=preorder[0]:
            left = preorder[1:]
            right = []
        else:
            left = preorder[1:i]
            right = preorder[i:]
        head.left = self.bstFromPreorder(left)
        head.right = self.bstFromPreorder(right)
        return head
