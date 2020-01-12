class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1,n):
            t,res = res,""
            j,k = 0,0
            while j<len(t):
                k = 0
                while j<len(t)-1 and t[j+1]==t[j]:
                    j += 1
                    k += 1
                res += str(k+1)+t[j]
                j += 1
        return res
