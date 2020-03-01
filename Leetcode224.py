class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res,operator,num = 0,1,0
        for i in s:
            if i=='(':
                stack.append(res)
                stack.append(operator)
                res,operator,num = 0,1,0
            elif i==')':
                res += num*operator
                num = 0
                res = res * stack.pop()
                res += stack.pop()
            elif i=='+':
                res += operator*num
                num,operator = 0,1
            elif i=='-':
                res += operator*num
                num,operator = 0,-1
            elif i!=' ':
                num = num*10 + int(i)
        res += operator*num
        return res
