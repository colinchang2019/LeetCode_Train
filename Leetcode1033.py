class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x = min([a,b,c])
        z = max([a,b,c])
        y = sum([a,b,c]) - x - z
        x,y = y-x-1,z-y-1
        #print(a,b,c,x,y)
        res = [0,0]
        if x==0 and y==0:
            res[0] = 0
        elif (x==0 and y!=0) or (x!=0 and y==0) or x==1 or y==1:
            res[0] = 1
        else:
            res[0] = 2
        res[1] += x+y
        return res
