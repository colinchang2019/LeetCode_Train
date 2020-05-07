# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return not t
        if not t:
            return True
        return self.full_same(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def full_same(self,a,b):
        if not a and not b: return True
        if a and b and a.val==b.val:
            return self.full_same(a.left,b.left) and self.full_same(a.right,b.right)
        return False
