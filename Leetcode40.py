class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(can,t,i,rest):
            if rest<=0:
                res.add(tuple(t))
                return
            if i>=len(can):
                return
            if can[i]<=rest:
                dfs(can,t+[can[i]],i+1,rest-can[i])
            dfs(can,t,i+1,rest)
            
        res = set()
        candidates = sorted(candidates)
        dfs(candidates,[],0,target)
        return [list(x) for x in res]


