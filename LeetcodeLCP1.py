class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        res = 0
        for i,x in enumerate(guess):
            if answer[i]==x:
                res += 1
        return res        
