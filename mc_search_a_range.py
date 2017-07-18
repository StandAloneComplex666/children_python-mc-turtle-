class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        c = 0
        if len(nums)==1 and nums[0]==target:
            res = [0,0]
            return res
        elif len(nums)==1 and nums[0]!=target:
            res=[-1,-1]
            return res
        for i in range(len(nums)):
            if (c == 1) and (nums[i] == target):
                res.append(i)
                return res
            elif (c == 0) and (nums[i] == target):
                if nums[i+1]==target
                res=[i,i]
                c = c + 1
        res=[-1,-1]
        return res
