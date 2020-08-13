class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1,num2 = num1[::-1],num2[::-1]
        n1,n2 = len(num1),len(num2)
        res,t = "",0
        for i in range(max(n1,n2)):
            if i<n1:
                t += int(num1[i])
            if i<n2:
                t += int(num2[i])
            t,t1 = divmod(t,10)
            res += str(t1)
        if t:
            res += str(t)
        return res[::-1]
