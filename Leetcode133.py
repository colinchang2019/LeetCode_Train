"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}

        def dfs(old):
            if old not in d:
                d[old] = new = Node(old.val,None)
                new.neighbors = [*map(dfs,old.neighbors)]
            return d[old]
        return dfs(node)
