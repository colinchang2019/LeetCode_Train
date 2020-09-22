# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        global res
        res = 0
        if not root:
            return 0
        if  self.dfs(root)==2:
            res += 1
        return res


    def dfs(self, root):
        # 0 该节点安装了显示器；1 该节点可观，但无显示器； 2 该节点不可见
        if not root:
            return 1
        left, right = self.dfs(root.left), self.dfs(root.right)
        if left==2 or right==2:
            global res
            res += 1 # 有一个儿子不可见，则父亲要安装监视器
            return 0
        elif left==0 or right==0:
            return 1 # 有一个儿子有监视器，则父亲可见
        else:
            return 2 # 所有儿子都可见无监视器，则父亲不可见，该父亲需要索求其父亲安装监视器
