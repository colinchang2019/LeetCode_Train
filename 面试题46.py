class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        d = [1]*(len(num)+1)
        p,q = 1,1
        for i in range(1,len(num)+1):
            a = 0
            if i>=2 and "09"<num[i-2:i]<"26":
                a = p
            p = q + a
            q,p = p,q
        return q
