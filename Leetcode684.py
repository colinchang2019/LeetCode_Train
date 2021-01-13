class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = {}
        p = {}
        for x in edges:
            if x[0]==8:
                print(d)
            if x[0] not in d and x[1] not in d:
                d[x[0]] = chr(x[0])
                d[x[1]] = chr(x[0])
                p[chr(x[0])] = [x[0], x[1]]
            elif x[0] not in d and x[1] in d:
                d[x[0]] = d[x[1]]
                p[d[x[1]]].append(x[0])
            elif x[0] in d and x[1] not in d:
                d[x[1]] = d[x[0]]
                p[d[x[0]]].append(x[1])
            else:
                if d[x[0]]==d[x[1]]:
                    return x
                p[d[x[0]]] += p[d[x[1]]]
                for j in p[d[x[1]]]:
                    d[j] = d[x[0]]
            if x==[1,7]:
                print(d)
