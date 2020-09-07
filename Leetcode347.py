class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, m, p = {},0,{}
        for i in nums:
            d[i] = d.get(i,0) + 1
            m = max(m,d[i])
        for i in d:
            p[d[i]] = p.get(d[i],[]) + [i]
        res = []
        for i in range(m,0,-1):
            if i in p:
                res += p[i]
            if len(res)>=k:
                return res
