class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n, res = len(arr), 0
        if n==1: return 0
        d = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d[i][i] = arr[i]
        for i in range(n-1):
            for j in range(i+1, n):
                d[i][j] = d[i][j-1] ^ arr[j]
                if d[i][j] == 0:
                    res += j - i
        return res
