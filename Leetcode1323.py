class Solution:
    def maximum69Number (self, num: int) -> int:
        res = list(str(num))
        for i in range(len(res)):
            if res[i]=='6':
                res[i] = '9'
                break
        return ''.join(res)
