class Solution:
    def countWords(self, w1: List[str], w2: List[str]) -> int:
        d1={}
        d2={}
        c=0
        for i in w1:
            d1[i]=d1.get(i,0)+1
        for i in w2:
            d2[i]=d2.get(i,0)+1
        for i in d1:
            if i in d2 and d1[i]==1 and d2[i]==1:
                c+=1
        return c
                
        