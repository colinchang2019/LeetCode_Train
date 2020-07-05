class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        d = [[False for _ in range(n+1)] for i in range(m+1)]
        d[0][0] = True
        for i in range(1,n+1):
            if p[i-1]=="*":
                d[0][i] = d[0][i-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == "*":
                    d[i][j] = d[i-1][j] or d[i][j-1]
                elif p[j-1]=="?" or p[j-1]==s[i-1]:
                    d[i][j] = d[i-1][j-1]
        return d[-1][-1]
