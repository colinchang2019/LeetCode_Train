"""
核心是：1)如果身高都相同，则所有人都按照k站队即可；2）如果有新的身高来，则新的身高都必须在相同k值得比它高的人前面——这样才能保证k值
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x:(-x[0],x[1]))
        res = []
        for p in people:
            res.insert(p[1],p)
        return res
