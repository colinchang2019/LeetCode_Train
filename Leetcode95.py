# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self.buildtree(1,n)
    
    def buildtree(self,start,end):
        res = []
        if start>end:
            res.append(None)
            return res
        else:
            for i in range(start,end+1):
                left_tree = self.buildtree(start,i-1)
                right_tree = self.buildtree(i+1,end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
