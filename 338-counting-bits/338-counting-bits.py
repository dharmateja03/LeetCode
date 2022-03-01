class Solution(object):
    def countBits(self, num):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[0]
        for i in range(1,num+1):
            if not i%2:
                l.append(l[i>>1])
            else:
                l.append(l[i-1]+1)
        return l