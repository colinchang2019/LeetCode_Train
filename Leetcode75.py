class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                t = stack.pop()
                res = max(res, (i-stack[-1]-1)*heights[t])
            stack.append(i)
        return res
