class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        ans=0
        ans= max(ans, min(h[l],h[r])*(r-l))
        while( l<len(h) and r>=0 and l<r):
            if l<len(h) and r>=0 and  h[l]<h[r]:
                l+=1
                print(l,r)
                ans= max(ans, min(h[l],h[r])*(r-l))
            else:
                r-=1
            
            ans= max(ans, min(h[l],h[r])*(r-l))
        return ans
                
                