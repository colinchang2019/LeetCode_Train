# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        def dfs(root):
            if not root: return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        self.li = dfs(root)
        self.index = -1
        self.le = len(self.li)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.li[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.index<self.le-1:
            return True
        return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
