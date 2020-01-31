class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = len(s)
        length = [len(x) for x in s]
        m = max(length)
        res = ['' for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if len(s[j])<=i:
                    res[i] += ' '
                else:
                    res[i] += s[j][i]
        return [x.rstrip() for x in res]
