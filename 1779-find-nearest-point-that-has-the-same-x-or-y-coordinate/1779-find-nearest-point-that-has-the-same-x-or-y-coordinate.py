class Solution:
    def nearestValidPoint(self, x: int, y: int, p: List[List[int]]) -> int:
        l=[x,y]
        ans=[]
        mn=11111111111111
        ans=-1
        for i in p:
            if i[0]==x or i[1]==y:
                if abs(x-i[0])+abs(y-i[1])<mn:
                    mn= abs(x-i[0])+abs(y-i[1])
                    ans=p.index(i)
        
        return ans