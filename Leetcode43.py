class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]*(len(num1)+len(num2))
        n1 = num1[::-1]
        n2 = num2[::-1]
        for i in range(len(num1)):
            tem = 0
            for j in range(len(num2)):
                tem += int(n1[i])*int(n2[j]) + res[i+j]
                res[i+j] = tem%10
                tem = tem //10
            res[i+j+1] += tem

        return str(int(''.join([str(x) for x in res[::-1]])))
