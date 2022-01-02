# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=0
        h=n-1
        while(l<=h):
            m=(l+h)//2
            if isBadVersion(m)==False:
                l=m+1
            else:h=m-1
        return l