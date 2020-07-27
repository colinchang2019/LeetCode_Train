class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1,t1 = len(s),len(t)
        if not s1:
            return True
        if t1<s1: return False
        d = [-1]*(t1+1)
        for i in range(t1):
            if t[i]==s[d[i]+1]:
                d[i+1] = d[i] + 1
                if d[i+1]==s1-1: return True
            else:
                d[i+1] = d[i]
        return False
