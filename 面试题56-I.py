class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = 0
        for x in nums:
            s ^=x # 通过或运算，得到x^y的结果
        lowbit = s&(-s) # 获得x^y结果后的最后一个1（二进制）
        a,b = 0,0
        for x in nums:
            if x&lowbit==lowbit: # 分成两组
                a^=x
            else:
                b^=x
        return [a,b]
