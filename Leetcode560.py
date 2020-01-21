class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        d[0] = 1
        su,res = 0,0
        for i in nums:
            su += i
            res += d.get(su-k,0)
            d[su] = d.get(su,0) + 1
        return res
