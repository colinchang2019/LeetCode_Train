class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(T))]
        tem = []
        for i,x in enumerate(T):
            while tem and tem[-1][1]<x:
                y = tem.pop()
                res[y[0]] = i-y[0]
            tem.append((i,x))
        return res
