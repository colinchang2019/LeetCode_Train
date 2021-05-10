# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1:
            return not root2
        if root1 and not root2:
            return False
        r1, r2 = self.dfs(root1, []), self.dfs(root2, [])
        # print(r1, r2)
        return r1==r2

    def dfs(self, root, res):
        t1 = self.leaf(root)
        if t1:
            res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
        return res

    def leaf(self, root):
        if not root.left and not root.right:
            return True
        return False
