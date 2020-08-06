class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        d = {} #翻转单词记录位置
        palidstr = [] # 记录本身就是回文单词
        for i,word in enumerate(words):
            d[word[::-1]] = i
            if word==word[::-1]:
                palidstr.append(i)
        for idx, word in enumerate(words):
            if word: #非空字符串
                for i in range(len(word)):
                    left,right = word[:i],word[i:]
                    if left==left[::-1] and right in d and idx!=d[right]:
                        res.append([d[right],idx])
                    if right==right[::-1] and left in d and idx!=d[left]:
                        res.append([idx,d[left]])
            else: # 空字符串
                for loc in palidstr:
                    if lov!=idx:
                        res.append([idx,loc])
        
        '''
        for i in range(len(words)):
            for j in range(len(words)): # 把这一步搜索转换为按单词长度的字典搜索
                if i==j: continue
                t = words[i]  + words[j]
                if t[::-1]==t:
                    res.append([i,j])
        '''

        return res
