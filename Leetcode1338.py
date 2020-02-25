class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        for i in arr:
            d[i] = d.get(i,0) + 1
        dic = [d[x] for x in d]
        dic = sorted(dic,reverse=True)
        res = 0
        for i,x in enumerate(dic):
            res += x
            if res>=(n+1)//2:
                return i+1
