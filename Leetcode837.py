class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        s = 0
        p = [0]*(K+W)
        for i in range(K,K+W):
            p[i] = 1 if i<=N else 0
            s += p[i]
        for i in range(K-1,-1,-1):
            p[i] = s/W
            s = s - p[i+W] + p[i]
        return p[0]
        '''
        定义p[i]为牌面i时的，未来能够获胜的概率。则p[i] = (p[i+1] +...+ p[i+W]/w)
        '''
