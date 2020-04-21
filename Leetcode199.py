# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        p = deque([]) # 存储奇数行
        q = deque([]) # 存储偶数行
        res = []
        p.append(root)
        while p or q:
            tem_p = [] # 存储奇数行
            tem_q = [] # 存储偶数行
            while p:
                x = p.popleft()
                tem_p.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            if tem_p:
                res.append(tem_p[-1])
            while q:
                x = q.popleft()
                tem_q.append(x.val)
                if x.left:
                    p.append(x.left)
                if x.right:
                    p.append(x.right)
            if tem_q:
                res.append(tem_q[-1])
        return res
