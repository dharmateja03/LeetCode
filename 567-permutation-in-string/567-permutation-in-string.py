class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        d2={}
        if len(s2)<len(s1):
            return 0
        for i in s1:
            d1[i]=d1.get(i,0)+1
        n=len(s1)
        for i in range(n):
            d2[s2[i]]=d2.get(s2[i],0)+1
        if d1==d2:
            return 1
        
        for i in range(n,len(s2)):
            if d1==d2:
                return 1
            d2[s2[i]]=d2.get(s2[i],0)+1
            d2[s2[i-n]]-=1
            if d2[s2[i-n]]==0:
                d2.pop(s2[i-n])
        if d1==d2:
            return 1
        return 0
            
        
        