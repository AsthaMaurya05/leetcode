class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l = []
        for i in accounts:
            l.append(sum(i))
        l.sort()
        return l[-1]   

