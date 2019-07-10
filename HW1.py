class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        slist=[]
        blist=[]
        elist=[]
        asum=0
        for i in range(len(nums)) :
            if nums[i] > (target/2.0):
                blist.append(i)
            if nums[i] < (target/2.0):
                slist.append(i)
            if nums[i] == (target/2.0):
                elist.append(i)
        if len(elist)==2:
            return elist
        else:
            for i in range(len(blist)):
                for j in range(len(slist)):
                    if (nums[blist[i]]+nums[slist[j]])== target:
                        if blist[i]>slist[j]:
                            tsum=[slist[j],blist[i]]
                        else:    
                            tsum=[blist[i],slist[j]]
        return tsum