class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        a,b = [0 for _ in range(26)],[0 for _ in range(26)]
        for i in ransomNote:
            a[ord(i)-97] += 1
        for i in magazine:
            b[ord(i)-97] += 1
        for i in range(26):
            if a[i]>b[i]:
                return False
        return True
