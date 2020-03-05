class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = []
        i = 1
        while candies>=i:
            res.append(i)
            candies -= i
            i += 1
        res.append(candies)
        r = [0]*num_people
        for i in range(len(res)):
            r[(i+1)%num_people-1] += res[i]
        return r
