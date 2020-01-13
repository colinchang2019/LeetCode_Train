class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res,d = 0,{}
        d['L'] = 0
        d['R'] = 0
        for j in s:
            d[j] += 1
            if d['L']==d['R']:
                d['L'] = 0
                d['R'] = 0
                res += 1
        return res
