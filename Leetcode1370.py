class Solution:
    def sortString(self, s: str) -> str:
        d, al, total, res = {}, [], len(s), ""
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in range(26):
            c = chr(i + ord("a"))
            if c in d:
                al.append([c, d[c]])
        n = len(al)
        while total>0:
            for i in range(n):
                if al[i][1]>0:
                    res += al[i][0]
                    al[i][1] -= 1
                    total -= 1
            for i in range(n-1, -1, -1):
                if al[i][1]>0:
                    res += al[i][0]
                    al[i][1] -= 1
                    total -= 1
        return res
