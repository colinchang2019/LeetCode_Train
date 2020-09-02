class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        b = [0,0,0,0,0,0] # 分别用来记录‘+’，‘-’，‘.’，'E','e',数字的个数
        if not s:
            return False
        a = list('0123456789')
        c = list('+-.eE')
        if s[-1] not in a+["."]:
            return False
        for i in range(len(s)):
            if s[i] == '+':
                b[0] += 1
                if i!=0 and s[i-1] not in ['e','E']:
                    return False
            if s[i] == '-':
                b[1] += 1
                if i!=0 and s[i-1] not in ['e','E']:
                    return False
            if s[i] =='.':
                b[2] += 1
                if b[2]>1 or 'e' in s[:i] or 'E' in s[:i]:
                    return False
            if s[i] =='E':
                b[3] += 1
                if (b[3]+b[4])>1 or b[5]==0:
                    return False
            if s[i] =='e':
                b[4] += 1
                if (b[3]+b[4])>1 or b[5]==0:
                    return False
            if s[i] not in a+c:
                return False
            if s[i] in a: b[5] += 1
        if b[5]<b[2]: return False
        return True
