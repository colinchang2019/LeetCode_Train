class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if not sentence:
            return 0
        d = set(dictionary)
        n = len(sentence)
        dp = [i for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(i):
                if sentence[j:i] in d:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[i-1]+1)
        return dp[-1]
