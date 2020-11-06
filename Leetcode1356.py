class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d,res = {},[]
        for i in arr:
            x,n = i,0
            while x:
                x = x&(x-1)
                n += 1
            d[n] = d.get(n, []) + [i]
        for i in sorted(d.keys()):
            res += sorted(d[i])
        return res
