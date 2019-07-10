class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans=[]
        a=0
        for i in range(len(digits)):
           a = (a*10)+digits[i]
        a+=1
        while (a != 0):
            ans.append(a%10)
            a=a//10
        ans.reverse()
        return ans