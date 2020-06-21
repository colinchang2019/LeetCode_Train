class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i,len(self.nums)):
            self.sums[j+1] += diff

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1]-self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
