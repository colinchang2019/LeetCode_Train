class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        p = []
        for i in num:
            while k>0 and len(p)>0 and i<p[-1]:
                p.pop()
                k -= 1
            p.append(i)
        res = p[:-k] if k else p
        return "".join(res).lstrip("0") or "0"
                
