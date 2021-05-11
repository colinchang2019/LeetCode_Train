class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        rall = reduce(xor, range(1, n + 1))
        term = encoded[1]
        for i in range(3, len(encoded), 2):
            term = term^encoded[i]
        res = [rall^term]
        for x in encoded:
            res.append(res[-1]^x)
        return res
