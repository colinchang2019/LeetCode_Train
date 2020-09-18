class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=0:
            return nums
        used = [False]*len(nums)
        res = []
        nums = sorted(nums)
        self.__dfs(nums,[],0,used,res)
        return res

        
        
        
    def __dfs(self,nums,pre,index,used,res):
        if index==len(nums):
            res.append(list(pre))
            return
        for i in range(len(nums)):
            if not used[i]:
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                
                pre.append(nums[i]) # 添加
                used[i] = True # 表示已经访问
                
                self.__dfs(nums,pre,index+1,used,res) # 每一个位置的元素选择都要遍历，采用递归方式
                
                used[i] = False # 逐层返回，重新释放选择空间————回溯法
                pre.pop() # 列表也同时释放
  
        
