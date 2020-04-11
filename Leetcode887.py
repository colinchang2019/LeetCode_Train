import math
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        d = [[0 for _ in range(K+1)] for i in range(N+1)]
        res = N
        for i in range(1,N+1):
            for j in range(1,K+1):
                if j==1:
                    d[i][j] = i
                    if d[i][j]>=N and i<res: res = i
                    continue
                if i==1:
                    d[i][j] = 1
                    if d[i][j]>=N and i<res: res = i
                    continue
                d[i][j] = 1 + d[i-1][j] + d[i-1][j-1]
                if d[i][j]>=N and i<res: res = i
        return res
        ## 鸡蛋掉落题
