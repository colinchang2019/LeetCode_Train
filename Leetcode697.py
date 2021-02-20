class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d, ma, res = {}, 0, len(nums)
        for i,x in enumerate(nums):
            d[x] = d.get(x, []) + [i]
            ma = max(len(d[x]), ma)
        for i in d:
            if len(d[i])==ma:
                res = min(res, d[i][-1] - d[i][0] + 1)
        return res
