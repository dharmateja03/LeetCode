class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        if len(s)==1:
            return s[0]
        
        while(len(s)>2):
            s.sort()
            
            s[-1]-=s[-2]
            s.pop(-2)
        s.sort()
        if s[0]==0:return s[1]
        else: return s[1]-s[0]
        return s
            
             
        