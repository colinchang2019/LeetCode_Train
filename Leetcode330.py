class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        lemma: if nums cover [1, x-1], then num+[x] can cover [1, 2x-1];
        follow this lemma, we can increase x from 1, to n.
        """
        res, x = 0,1
        length, index = len(nums), 0
        while x<=n:
            if index<length and nums[index]<=x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                res += 1
        return res
