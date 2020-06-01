class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        res = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_candy:
                res[i] = True
        return res
