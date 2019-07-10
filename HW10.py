class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == []:
            return 0
        l = 0
        r = 0
        for i in range(len(S)):
            if S[i] == '(':
                l += 1
            else:
                if l != 0:
                    l -= 1
                else:
                    r += 1
        ans = l + r
        return ans