from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d1,d2 = set(),set()
        visited = [False]*len(graph)
        s = deque()
        for i in range(len(graph)):
            if graph[i] and not visited[i]:
                d1.add(i)
                d2.update(graph[i])
                s = deque(graph[i])
                visited[i] = True
                if not self.bfs(visited,d1,d2,s,graph):
                    return False
        return True
    
    def bfs(self,visited,d1,d2,s,graph):
        while s:
            x = s.popleft()
            if visited[x]:
                continue
            y = graph[x]
            if x in d1:
                for i in y:
                    if i in d1:
                        return False
                d2.update(y)
            if x in d2:
                for i in y:
                    if i in d2:
                        return False
                d1.update(y)
            s += y
            visited[x] = True
        return True
