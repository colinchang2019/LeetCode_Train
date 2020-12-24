class Solution:
    def candy(self, ratings: List[int]) -> int:
        g = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1] and g[i]<=g[i-1]:
                g[i] = g[i-1] + 1
        for i in range(1, len(ratings)):
            t = len(ratings)-1-i
            if ratings[t]>ratings[t+1] and g[t]<=g[t+1]:
                g[t]=g[t+1]+1
        return sum(g)
