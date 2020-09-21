# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        d1,p = {},root
        def dfs(p):
            if not p:
                return []
            return dfs(p.left) + [p.val] + dfs(p.right)
        d = dfs(p)
        if len(d)<2:
            return root
        for i in range(len(d)-2,-1,-1):
            d1[d[i]] = d[i] + d[i+1]
            d[i] += d[i+1]
        d1[d[-1]] = d[-1]
        q = root
        def dfs2(q):
            if not q:
                return 
            q.val = d1[q.val]
            dfs2(q.left)
            dfs2(q.right)
        dfs2(q)
        return root
        
