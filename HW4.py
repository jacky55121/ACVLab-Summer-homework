class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z=0
        x1=x
        if x>=0:
            while (x != 0):
                z=(z*10)+(x%10)
                x=x//10
            if x1==z:
                return True
            else:
                return False
        else:
            return False