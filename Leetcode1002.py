class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A)<2:
            return list(A[0])
        n = len(A)
        import numpy as np
        d = np.array([[0 for _ in range(26)] for i in range(n)])
        for i in range(n):
            for x in A[i]:
                d[i,ord(x)-97] += 1
        d = d.T
        res = ""
        for i in range(26):
            t = min(d[i])
            res += chr(i+97)*t
        return list(res)
