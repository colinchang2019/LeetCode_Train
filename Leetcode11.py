class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0,len(height)-1
        maxArea = 0
        while i < j:
            if height[i]<=height[j]:
                maxArea = max(maxArea,height[i]*(j-i))
                i += 1
            else:
                maxArea = max(maxArea,height[j]*(j-i))
                j -= 1
        return maxArea
