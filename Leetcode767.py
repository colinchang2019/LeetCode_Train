class Solution:
    def reorganizeString(self, S: str) -> str:
        from collections import Counter
        b, n = Counter(S), len(S)
        d = [[x, b[x]] for x in b]
        d = sorted(d,  key=lambda x:x[1], reverse=True)
        if d[0][1]>(n+1)/2: return ""
        res, x = [""]*len(S), 0
        for i in range(0, n, 2):
            if d[x][1]==0:
                x += 1
            res[i] = d[x][0]
            d[x][1] -= 1
        for i in range(1, n, 2):
            if d[x][1]==0:
                x += 1
            res[i] = d[x][0]
            d[x][1] -= 1
        #print(res)
        return "".join(res)
