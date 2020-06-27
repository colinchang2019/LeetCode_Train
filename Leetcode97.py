class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,l = len(s1),len(s2),len(s3)
        if m+n!=l:
            return False
        d = [[False for i in range(m+1)] for _ in range(n+1)]
        d[0][0] = True
        for i in range(1,n+1):
            d[i][0] = (d[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,m+1):
            d[0][i] = (d[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,n+1):
            for j in range(1,m+1):
                d[i][j] = (d[i][j-1] and s2[j-1]==s3[i+j-1]) or (d[i-1][j] and s1[i-1]==s3[i+j-1])
        # print(d)
        return d[-1][-1]
