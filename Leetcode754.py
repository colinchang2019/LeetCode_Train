class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        su = 0
        i = 1
        while True:
            su += i
            if su>=target and (su-target)%2==0:
                return i
            i += 1
