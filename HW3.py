class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        z=0
        a=1
        if x<0:
            x=x*(-1)
            a=-1
        while (x != 0):
            z=(z*10)+(x%10)
            x=x//10
        z=z*a
        if (z < -2147483648) or (z > 2147483647):
            z=0
        return z