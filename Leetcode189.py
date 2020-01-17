class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return 
        n = len(nums)
        k %= n
        nums[:n-k] = nums[n-k-1::-1]
        nums[n-k:] = nums[n-1:n-k-1:-1]
        nums[:] = nums[::-1]
