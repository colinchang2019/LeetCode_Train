class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mark,res = 0,0
        for i in range(len(nums)):
            if nums[i]==0:
                res = max(res, mark)
                mark = 0
            else:
                mark += 1
        return max(res, mark)
