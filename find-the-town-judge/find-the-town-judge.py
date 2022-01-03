class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        l=[0]*(n+1)
        if len(t)==0 and n==1:
            return 1
        #a,b--> a trust b
        for i in range(len(t)):
            l[t[i][0]]-=1
            l[t[i][1]]+=1
        for i in l:
            if i==n-1:
                return l.index(i)
        return -1
            
        
        
        