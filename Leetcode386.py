class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1,10):
            self.dfs(i,n,res)
        return res
        
    def dfs(self,i,n,res):
        if i>n:
            return 
        res.append(i)
        i *= 10
        for j in range(10):
            self.dfs(i+j,n,res)
## 上面是利用递归做的
