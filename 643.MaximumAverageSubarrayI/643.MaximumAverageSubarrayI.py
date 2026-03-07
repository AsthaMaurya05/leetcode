class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s=0
        for i in range(k):
            s+=nums[i]
        avg = s*1.0/k    
        for i in range(k,len(nums)):
            s += nums[i]-nums[i-k]
            if avg < s*1.0/k :
                avg = s*1.0/k
        return avg        

        
       