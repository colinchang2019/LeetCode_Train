class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 组合公式c(n,i) = n!/(i!*(n-i)!)
        # 第i+1项是第i项的(n-i)/(i+1)
        res = []
        t = 1
        for i in range(rowIndex+1):
            res.append(t)
            t = t * (rowIndex-i)/(i+1)
        return res
