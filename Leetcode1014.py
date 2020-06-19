class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        mx = 0 # 用来记录当前最大的A[i] + i
        res = 0 # 用来记录最终结果
        for i in range(len(A)):
            if i==0:
                mx = A[i] + i
                continue
            res = max(res, A[i]-i+mx)
            mx = max(mx, A[i]+i)
        return res
