from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        t = p
        if len(t)>len(s):
            return []
        res = []
        d1 = Counter(t)
        d = {}
        l,r = 0,0
        while r<len(s):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            r += 1
            #print(l,d)
            if self.check(d1,d):
                #print(l,d)
                res.append(l)
                d[s[l]] -= 1
                l += 1
            if r-l>=len(t):
                d[s[l]] -= 1
                l += 1
            if r==len(s):break
            
        return res
    
    def check(self,d1,d2):
        for x in d1:
            if x not in d2 or d2[x]!=d1[x]:
                return False
        return True
