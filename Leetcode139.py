class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic,diclen = {},[]
        for i in wordDict:
            dic[i] = 0
            if len(i) not in diclen:
                diclen.append(len(i))
        diclen.sort()
        d = [False for _ in range(len(s)+1)]
        d[0] = True
        for i in range(1,len(s)+1):
            for j in diclen:
                if j>i:
                    break
                if s[i-j:i] in dic and d[i-j]:
                    d[i] = True
        return d[-1]
