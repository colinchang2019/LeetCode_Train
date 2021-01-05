class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res, i, a = [], 0, 0
        if len(s)<3:
            return res
        while i<len(s)-1:
            while i<len(s)-1 and s[i+1]==s[i]:
                i += 1
            if i-a+1>=3:
                res.append([a, i])
            i += 1
            a = i
        return res
