class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0]
        for i in nums:
            self.nums.append(self.nums[-1]+i)
        
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1]-self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
