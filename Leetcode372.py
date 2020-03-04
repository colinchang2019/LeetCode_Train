class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        a = a%1337
        for i in b:
            res = (pow(res,10)%1337) * (pow(a,i)%1337) %1337
        return res
