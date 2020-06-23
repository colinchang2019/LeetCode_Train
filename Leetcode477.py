class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(32):
            n1 = 0
            for j in range(n):
                n1 += (nums[j]>>i)&1
            res += (n-n1)*n1
        return res
