class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = [False for i in range(len(friends))]
        visited[id] = True
        lev = []
        l1 = [id]
        l2 = []
        while l1 or l2:
            while l1:
                x = l1.pop()
                for i in friends[x]:
                    if not visited[i]:
                        l2.append(i)
                        visited[i] = True
            lev.append(l2.copy())
            while l2:
                x = l2.pop()
                for i in friends[x]:
                    if not visited[i]:
                        l1.append(i)
                        visited[i] = True
            lev.append(l1.copy())
            if len(lev)>=level:
                break
        d = {}
        for i in lev[level-1]:
            for j in watchedVideos[i]:
                d[j] = d.get(j,0) + 1
        res = [(i,d[i]) for i in d]
        res = sorted(res,key=lambda x:(x[1],x[0]))
        return [x[0] for x in res]
