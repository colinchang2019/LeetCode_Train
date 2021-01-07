class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0
        n, m = 0, len(isConnected)
        visited = [False]*len(isConnected)
        for i in range(m):
            if visited[i]:
                continue
            from collections import deque
            a = deque([i])
            while a:
                x = a.popleft()
                visited[x] = True
                for j in range(m):
                    if not visited[j] and isConnected[x][j]:
                        a.append(j)
            n += 1
        return n

