class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split(".")
        s2 = version2.split(".")
        if len(s1)<len(s2):
            s1 += ["0"]*(len(s2)-len(s1))
        else:
            s2 += ["0"]*(len(s1) - len(s2))
        for i in range(len(s1)):
            p,q = s1[i],s2[i]
            if len(p)<len(q):
                p = "0"*(len(q)-len(p)) + p
            else:
                q = "0"*(len(p)-len(q)) + q
            if p>q:
                return 1
            elif p<q:
                return -1
            else:
                continue
        return 0
