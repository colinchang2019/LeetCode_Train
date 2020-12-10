class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        t = [0, 0, 0]  # 分别表示三种现金的数额
        for char in bills:
            if char == 5:
                t[0] += 1
            elif char == 10:
                if t[0] == 0:
                    return False
                else:
                    t[0] -= 1
                    t[1] += 1
            else:
                if t[0] > 0 and t[1]>0:
                    t[0] -= 1
                    t[1] -= 1
                    t[2] += 1
                elif t[0] >= 3 and t[1] <= 0:
                    t[0] -= 3
                    t[2] += 1
                else:
                    return False
        return True
