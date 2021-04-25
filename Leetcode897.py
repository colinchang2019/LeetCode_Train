# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        return self.dfs(root)[0]
        
    
    def dfs(self, root):
        if root and not root.left and not root.right:
            return root, root

        if not root.left and root.right:
            right1, right2 = self.dfs(root.right)
            root.right = right1
            return root, right2
        
        if root.left and not root.right:
            left1, left2 = self.dfs(root.left)
            left2.right = root
            root.left = None
            return left1, root
        left1, left2 = self.dfs(root.left)
        right1, right2 = self.dfs(root.right)
        left2.right = root
        root.right = right1
        root.left = None
        return left1, right2
