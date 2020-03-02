class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res,operator,num = 0,1,0
        stack.append(operator)
        for i in s:
            if i=='*':
                stack.append(num)
                stack.append("*")
                num = 0
            elif i=='/':
                stack.append(num)
                stack.append("/")
                num = 0
            elif i=='+' or i=='-':
                stack.append(num)
                tem = stack[0]
                pre = "*"
                for j in range(1,len(stack)):
                    if stack[j]=="*" or stack[j]=="/":
                        pre = stack[j]
                    else:
                        tem = tem*stack[j] if pre=="*" else tem//stack[j]
                stack = []
                res += operator*tem
                num = 0
                operator = 1 if i=='+' else -1
            elif i!=' ':
                num = num*10 + int(i)
        # print(stack,num,operator)
        stack.append(num)
        tem = stack[0]
        pre = "*"
        for j in range(1,len(stack)):
            if stack[j]=="*" or stack[j]=="/":
                pre = stack[j]
            else:
                tem = tem*stack[j] if pre=="*" else tem//stack[j]
        res += operator*tem
        return res
