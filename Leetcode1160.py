class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for x in chars:
            d[x] = d.get(x,0) + 1
        res = 0
        for x in words:
            if self.isin(x,d):
                res += len(x)
        return res

    def isin(self,x,d):
        d1 = d.copy()
        for i in x:
            if d1.get(i,0)<=0:
                return False
            else:
                d1[i] = d1.get(i,0) - 1
        return True
