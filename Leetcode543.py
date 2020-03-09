# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    

    def dfs(self,root):
        if not root:
            return 0
        x = self.dfs(root.left)
        y = self.dfs(root.right)
        self.res = max(self.res,x+y)
        return max(x,y)+1
