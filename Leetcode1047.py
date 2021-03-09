class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for i in S:
            if res and res[-1]==i:
                res.pop()
            else:
                res.append(i)
        return "".join(res)
