class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d,res = {},[]
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        if not digits:
            return res
        res = [x for x in d[digits[0]]]
        for i in digits[1:]:
            res = [x+y for x in res for y in d[i]]
        return res
