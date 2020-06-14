class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        pre = 0
        for i,a in enumerate(arr):
            k = len(arr) - i
            d = pre + a*k - target
            if d>0:
                return a-d//k-(2*(d%k)>=k)
            pre += a
        return arr[-1]
