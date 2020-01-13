# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            p,q = root.left,root.right
            pl,pr = root,root
            root.left = None
            if p:
                pl,pr = dfs(p)
                root.right = pl
            ql,qr = pr,pr
            if q:
                ql,qr = dfs(q)
                pr.right = ql
            return root,qr
        
        if root:
            dfs(root)
