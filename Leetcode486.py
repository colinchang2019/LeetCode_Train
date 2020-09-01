from collections import deque
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # p = deque(nums)


        def total(s,t,flag):
            if s==t: return nums[s]*flag
            score_s = nums[s]*flag + total(s+1,t,-flag)
            score_t = nums[t]*flag + total(s,t-1,-flag)
            return max(score_s*flag,score_t*flag)*flag
        return total(0,len(nums)-1,1)>=0
