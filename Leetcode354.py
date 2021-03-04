class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n<=1:
            return n
        envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        d,res = [1]*n,1
        for i in range(1,n):
            for j in range(i):
                if envelopes[i][1]>envelopes[j][1]:
                    d[i] = max(d[i], d[j]+1)
            res = max(res, d[i])
        return res
