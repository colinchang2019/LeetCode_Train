class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return n
        elif n==2:
            return 1 if arr[0]==arr[1] else 2
        flag = 0
        maxn, mark = 1, 1
        for i in range(1, len(arr)):
            if arr[i]==arr[i-1]:
                maxn = max(maxn, mark)
                # print(i, maxn)
                flag,mark = 0,1
                continue
            if i==1:
                flag = -1 if arr[i]<arr[i-1] else 1
                mark = 2
            else:
                flag1 = -1 if arr[i]<arr[i-1] else 1
                if flag!=flag1:
                    mark += 1
                    flag = flag1
                else:
                    maxn = max(maxn, mark)
                    #　print(i, maxn)
                    mark = 2
        maxn = max(mark, maxn)
        return maxn
