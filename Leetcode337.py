# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))


    def dp(self,root):
        if not root: return 0,0
        ls,ln = self.dp(root.left)
        rs,rn = self.dp(root.right)
        return root.val + ln + rn, max(ls,ln) + max(rs,rn)
