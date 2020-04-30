class Solution:
    def isHappy(self, n: int) -> bool:
        slow = str(n)
        fast = str(sum([int(i)**2 for i in str(n)]))
        while slow!=fast:
            slow = str(sum([int(i)**2 for i in slow]))
            fast = str(sum([int(i)**2 for i in fast]))
            fast = str(sum([int(i)**2 for i in fast]))
        return slow=='1'
