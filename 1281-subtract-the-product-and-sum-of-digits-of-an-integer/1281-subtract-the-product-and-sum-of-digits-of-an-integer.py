class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l=list(map(int,str(n)))
        ans=1
        for i in l:
            ans=i*ans
        return ans-sum(l)
        