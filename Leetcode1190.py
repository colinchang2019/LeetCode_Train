class Solution:
    def reverseParentheses(self, s: str) -> str:
        k, res = [], ""
        for i in range(len(s)):
            if s[i]==")":
                #print(res, k)
                res = res[:k[-1]] + " " + res[k[-1]+1:][::-1] + " "
                k.pop()
                #print("modify: ", res)
            else:
                res += s[i]
                if s[i]=="(":
                    k.append(i)
        return res.replace(" ", "")
