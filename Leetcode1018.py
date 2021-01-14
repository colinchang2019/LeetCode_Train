class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        x = 0
        for i in A:
            x <<= 1
            x += i
            res.append(True if x%5==0 else False)
        return res
