class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0 or shorter==longer==0:
            return []
        if shorter==longer:
            return [k*shorter]
        res = []
        dic = {}
        for i in range(k+1):
            t = i*longer + (k-i)*shorter
            if t in dic:
                continue
            dic[t] = 1
            res.append(t)
        return res
