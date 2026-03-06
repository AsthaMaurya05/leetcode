class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = nums[0]
        sum = 0
        for i in nums:
            sum = sum+i
            if sum> mx:
                mx = sum
            if sum<0:
                sum=0
        return mx