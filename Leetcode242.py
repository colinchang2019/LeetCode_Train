class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1 = [0 for _ in range(26)]
        d2 = [0 for _ in range(26)]
        for i in s:
            d1[ord(i)-97] += 1
        for i in t:
            d2[ord(i)-97] += 1
        return d1==d2
