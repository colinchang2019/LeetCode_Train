class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        a = str(N)
        i,n,flag = 0,len(a),False
        if n<2:
            return N
        for i in range(n-1):
            if a[i]>a[i+1]:
                flag = True
                break
        if not flag:
            return N
        while i>0 and a[i-1]==a[i]:
            i -= 1
        # print(i)
        res = a[:i] + chr(ord(a[i]) - 1) + "9"*(n - i - 1)
        return int(res.lstrip("0"))
