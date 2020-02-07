class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        d = [1 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                d[i] = d[i-1] + 1
            if d[i]==k:
                break
        if d[i]==k:
            # print(s[:i-k+1]+s[i+1:])
            del d
            return self.removeDuplicates(s[:i-k+1]+s[i+1:],k)
        return s
