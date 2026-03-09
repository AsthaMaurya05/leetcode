class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [str(i) for i in nums]
        even = 0
        for i in l:
            if (len(i)%2==0):
                even+=1
        return even        


