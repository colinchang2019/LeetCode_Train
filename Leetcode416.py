class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 分割等和子集；
        target = sum(nums)
        if target%2==1:
            return False
        target = target//2
        d = [False for _ in range(target+1)]
        d[0] = True
        for i in range(len(nums)):
            for j in range(nums[i],target+1)[::-1]:
                if i==0:
                    d[j] = (nums[i]==j)
                else:
                    d[j] = d[j] or d[j-nums[i]]
        return d[-1]
