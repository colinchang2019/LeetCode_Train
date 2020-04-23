class Solution:
    def waysToChange(self, n: int) -> int:
        d = [1] + [0]*n
        for c in [1,5,10,25]:
            for i in range(c,n+1):
                d[i] += d[i-c]
        return d[-1]%1000000007
