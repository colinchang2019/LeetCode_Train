class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d1,d2 = {},{}
        res = 0
        for i in A:
            for j in B:
                if i+j in d1:
                    d1[i+j] += 1
                else:
                    d1[i+j] = 1
        for i in C:
            for j in D:
                if -(i+j) in d1:
                    res += d1[-(i+j)]
        return res
