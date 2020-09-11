class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(can,t,i,rest,k):
            if rest<=0 and len(t)==k:
                res.append(t)
                return
            if i>=len(can) or len(t)>k:
                return
            if can[i]<=rest:
                dfs(can,t+[can[i]],i+1,rest-can[i],k)
            dfs(can,t,i+1,rest,k)
            
        res = []
        candidates = [1,2,3,4,5,6,7,8,9]
        dfs(candidates,[],0,n,k)
        return res
