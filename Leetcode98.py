# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root):
            ml = mr = root.val
            flag1 = flag2 = True
            if root.left:
                if root.left.val>=root.val:
                    return 0,0,False
                else:
                    a,b,flag1 = dfs(root.left)
                    ml,flag1 = a,(flag1 and root.val>b)
            if root.right:
                if root.right.val<=root.val:
                    return 0,0,False
                else:
                    a,b,flag2 = dfs(root.right)
                    mr,flag2 = b,(flag2 and root.val<a)
            return ml,mr,(flag1 and flag2)
        if not root:
            return True
        return dfs(root)[2]
