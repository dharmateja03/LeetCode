class Solution:
    def canPlaceFlowers(self, l: List[int], n: int) -> bool:
        l=[0]+l+[0]
        for i in range(1,len(l)-1):
            if l[i-1]==0 and l[i+1]==0 and l[i]==0:
                l[i]=1
                n-=1
            
       
        if n<1:
            return 1
        return 0
        