from collections import deque
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        p = deque([(0,0)])
        dire = [(-1,0),(0,-1),(0,1),(1,0)]
        visited = [[False for _ in range(n)] for i in range(m)]
        visited[0][0] = True
        res = 0
        while p:
            x,y = p.popleft()
            #print((x,y))
            res += 1
            for ix,iy in dire:
                xn,yn = x+ix,y+iy
                if 0<=xn<m and 0<=yn<n and not visited[xn][yn] and self.com(xn,yn,k):
                    p.append((xn,yn))
                    visited[xn][yn] = True
        return res
    
    def com(self,x,y,k):
        return sum([int(t) for t in str(x)+str(y)])<=k
