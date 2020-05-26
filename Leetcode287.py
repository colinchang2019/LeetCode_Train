class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set(nums)
        return (sum(nums)-sum(a))//(len(nums)-len(a))
