class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        max_len = 0
        for num in nums:
            if num not in d:
                left = d.get(num-1,0)
                right = d.get(num+1,0)
                
                cur_len = 1+left +right
                max_len = max(cur_len,max_len)
                
                d[num] = cur_len
                d[num-left] = cur_len
                d[num+right] = cur_len # 将边缘两个点指向明确掉，因为下一个连接长度集合的只有两端
        return max_len
