class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:return 1
        if n%3!=0 or n<=0:return 0
        return Solution.isPowerOfThree(self,n/3)
        