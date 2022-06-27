class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        l,r=0,len(c)-k
        t=sum(c[r:])
        ans=t
        while(r<len(c)):
            t+=(c[l]-c[r])
            r+=1
            l+=1
            ans=max(ans,t)
        return ans
            
        