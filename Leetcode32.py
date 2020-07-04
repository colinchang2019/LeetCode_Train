class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<=1:
            return 0
        d = [0 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]==")" and s[i-1]=="(":
                d[i] = d[i-2] + 2 if i>=2 else 2
            if s[i]==")" and s[i-1]==")" and i-d[i-1]-1>=0 and s[i-d[i-1]-1]=="(":
                d[i] = d[i-1] + d[i-d[i-1] - 2] + 2 if i-d[i-1]>=2 else d[i-1]+2
        # print(d)
        return max(d)
