class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<3:
            return 0
        count = 0
        for i in range(2,len(s)):
            if s[i]!=s[i-1] and s[i]!=s[i-2] and s[i-1]!=s[i-2]:
                count+=1
        return count