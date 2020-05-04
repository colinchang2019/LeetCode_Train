class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心算法，每一步都选择当前最优的——即在步i范围内能迈出最远的地方
        end,max_position,step = 0,0,0
        for i in range(len(nums)-1):
            max_position = max(max_position, i+nums[i])
            if i==end:
                end = max_position
                step += 1
        return step
