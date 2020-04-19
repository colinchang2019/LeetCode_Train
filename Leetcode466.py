class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1==0: return 0
        s1cnt,index,s2cnt = 0,0,0
        re = {}
        while True:
            s1cnt += 1
            for ch in s1:
                if ch==s2[index]:
                    index += 1
                    if index ==len(s2):
                        s2cnt,index = s2cnt+1,0
            if s1cnt==n1: # 走完所有s1都没有产生循环
                return s2cnt//n2
            
            if index in re:# 记录每一次s1结束后index 的位置
                s1_p,s2_p = re[index]
                pre_loop = (s1_p,s2_p)
                in_loop = (s1cnt - s1_p,s2cnt-s2_p)
                break
            else:
                re[index] = (s1cnt,s2cnt)
        res = pre_loop[1] + (n1-pre_loop[0])//in_loop[0]*in_loop[1]
        rest = (n1-pre_loop[0])%in_loop[0]
        for i in range(rest):
            for ch in s1:
                if ch==s2[index]:
                    index += 1
                    if index ==len(s2):
                        res,index = res+1,0
        return res//n2
