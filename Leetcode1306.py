class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False for _ in range(len(arr))]
        vis[start] = True
        if arr[start]==0:
            return True
        else:
            return self.dfs(vis,start,arr,n)


    def dfs(self,vis,st,arr,n):
        left,right = st - arr[st],st + arr[st]
        if 0<=left<n and not vis[left]:
            if arr[left]==0:
                return True
            else:
                vis[left] = True
                if self.dfs(vis,left,arr,n):
                    return True
            vis[left] = False
        if 0<=right<n and not vis[right]:
            if arr[right]==0:
                return True
            else:
                vis[right] = True
                if self.dfs(vis,right,arr,n):
                    return True
            vis[right] = False
        return False
