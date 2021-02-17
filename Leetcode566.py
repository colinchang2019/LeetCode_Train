class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r1,c1 = len(nums), len(nums[0])
        if r1*c1!=r*c:
            return nums
        mark, res = [],[]
        for x in nums:
            mark += x
        for i in range(r):
            res.append(mark[i*c:(i+1)*c])
        return res
