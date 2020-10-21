class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j,n,m = 0,len(typed),len(name)
        if n<m: return False
        for i in range(m):
            # print(i,j)
            if j<n and typed[j]==name[i]:
                j += 1
            elif j<n and i>0 and typed[j]==name[i-1]:
                while j<n and typed[j]==name[i-1]:
                    j += 1
                if j<n and typed[j]==name[i]:
                    j += 1
                    continue
                else:
                    return False
            else:
                return False
        while j<n and typed[j]==name[i]:
            j += 1
        print(i,j)
        if (j==n-1 and typed[j]==name[i]) or j>n-1:
            return True
        else:
            return False
