class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 利用前缀和的概念
        pre = [0]
        for i in arr:
            pre.append(pre[-1]^i)
        return [pre[a]^pre[b+1] for a,b in queries]
