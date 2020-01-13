"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        p,q = deque(),deque()
        p.append(root)
        while p or q:
            while p:
                x = p.popleft()
                x.next = None if not p else p[0]
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            while q:
                x = q.popleft()
                x.next = None if not q else q[0]
                if x.left:
                    p.append(x.left)
                if x.right:
                    p.append(x.right)
        return root
