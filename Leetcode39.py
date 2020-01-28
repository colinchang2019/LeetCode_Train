class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if len(candidates)==0:
            return res
        
        def backtrack(candidates,target,su,index,res,path):
            if su==target:
                # print(path,candidates[index])
                res.append(path.copy())
            elif su>target:
                return 
            else:
                for i in range(index,len(candidates)):
                    path.append(candidates[i])
                    su += candidates[i]
                    backtrack(candidates,target,su,i,res,path)
                    path.pop()
                    su -= candidates[i]
        backtrack(candidates,target,0,0,res,[])
        return res
