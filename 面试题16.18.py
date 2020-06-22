class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        n = len(value)
        flag = True
        a_cnt,b_cnt = pattern.count("a"),pattern.count("b")
        a_max_len = 0 if a_cnt==0 else n//a_cnt  # 用来表示a匹配的字符串最大长度
        for a_l in range(a_max_len+1): # 遍历所有a可能匹配字符串的长度
            if not b_cnt: #　在每一种可能情况下，首先判断ｂ是否存在
                if n!=a_l*a_cnt:
                    continue
                b_l = 0
            else:
                b_total_l = n - a_cnt*a_l
                if b_total_l%b_cnt!=0: # 如果当前长度下，没法完美分配，结束
                    continue
                b_l = b_total_l//b_cnt
            a,b = None,None
            i = 0
            flag = True
            for p in pattern:
                if p=="a":
                    s = value[i:(i+a_l)]
                    i += a_l
                    if a is not None and a!=s:
                        flag = False
                        break
                    a = s
                else:
                    s = value[i:(i+b_l)]
                    i += b_l
                    if b is not None and b!=s:
                        flag = False
                        break
                    b = s
            if flag and a!=b:
                return True
        return False
