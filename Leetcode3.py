class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        res = 0
        l,r = 0,0
        while l<len(s):
            while r+1<len(s) and (s[r+1] not in s[l:r+1]):
                r += 1
            res = max(res,r - l + 1)
            l += 1
        return res
        
