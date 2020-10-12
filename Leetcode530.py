# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        def mid(root):
            if not root:
                return []
            return mid(root.left) + [root.val] + mid(root.right)
        arr = mid(root)
        s = arr[1] - arr[0]
        for i in range(len(arr)-1):
            s = min(s, arr[i+1]-arr[i])
        return s
