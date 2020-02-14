class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left,right = min([a,b,c]),min([a,b,c])*n
        while left<right:
            x = (left+right)//2
            mab = self.mcn(a,b)
            num = x//a+x//b+x//c-x//mab-x//self.mcn(a,c)-x//self.mcn(b,c)+x//self.mcn(mab,c)
            if num>n:
                right = x - 1
            elif num<n:
                left = x + 1
            else:
                left = x
                break
        return left - min([left%a,left%b,left%c])

    def mcn(self,a,b):
        m = a*b
        while b>0:
            a,b = b,a%b
        return m/a
