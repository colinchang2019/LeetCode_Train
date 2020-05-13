# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        if root:
            t = str(root.val)
            self.dfs(root,t)
        return self.res

    def dfs(self,root,t):
        if not root.left and not root.right:
            self.res.append(t)
        if root.left:
            t_l = t + "->" + str(root.left.val)
            self.dfs(root.left,t_l)
        if root.right:
            t_r = t + "->" + str(root.right.val)
            self.dfs(root.right,t_r)
