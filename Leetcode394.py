class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        num = []
        tem = []
        for i in s:
            if i.isdigit():
                if not num or type(num[-1])!=str:
                    num.append(i)
                else:
                    num[-1] += i
            elif i=='[':
                num[-1] = int(num[-1])
                if tem:
                    tem.append('')
                continue
            elif i==']':
                t = tem[-1]*num[-1]
                tem.pop()
                num.pop()
                if tem:
                    tem[-1] = tem[-1] + t
                elif num:
                    tem.append(t)
                else:
                    res += t
            else:
                if tem:
                    tem[-1] += i
                else:
                    tem.append(i)
        if tem:
            res += tem[-1]
        return res
