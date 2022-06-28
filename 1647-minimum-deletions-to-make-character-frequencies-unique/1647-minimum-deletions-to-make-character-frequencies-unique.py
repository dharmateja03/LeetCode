class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        ans=0
        l=list(d.values())
        print(l)
        s=set()
        for i in l:
            while(i in s and i>0):
                i-=1 
                ans+=1
            s.add(i)
        return ans
        
        