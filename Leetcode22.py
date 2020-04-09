class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur_str = ""
        def dfs(cur_str, left, right):
            if left==right==0:
                res.append(cur_str)
            if left>right:
                return
            if left>0:
                dfs(cur_str+"(", left-1, right)
            if right>0:
                dfs(cur_str+")", left, right-1)
        dfs(cur_str, n, n)
        return res
