class Solution:
    def smallestSubsequence(self, s: str) -> str:
        rest, pre, stack = Counter(s), set(), []
        for x in s:
            if x not in pre:
                while stack and  stack[-1]>x and  rest[stack[-1]]>0:
                    pre.remove(stack.pop())
                stack.append(x)
                pre.add(x)
            rest[x] -= 1
        return "".join(stack)
