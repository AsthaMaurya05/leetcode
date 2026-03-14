
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t_sum = sum(nums)
        l_sum = 0
        for i, num in enumerate(nums):
            if l_sum == t_sum - l_sum - num:
                return i
            l_sum += num
        return -1
        
    
        
        
        
        