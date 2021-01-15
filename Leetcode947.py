class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dx, dy = {}, {}
        for x,y in stones:
            dx[x] = dx.get(x, []) + [(x, y)]
            dy[y] = dy.get(y, []) + [(x, y)]
        visited = set()
        def dfs(node):
            if node in visited: return 
            x, y = node
            visited.add((x, y))
            for i in dx[x]:
                dfs(i)
            for i in dy[y]:
                dfs(i)
        
        res = 0
        for i in stones:
            i = tuple(i)
            if i not in visited:
                res += 1
                dfs(i)
        return len(stones) - res
