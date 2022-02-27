class Solution:
    def distributeCandies(self, c: List[int]) -> int:
        d={}
        for i in c:
            d[i]=d.get(i,0)+1
        if len(list(d.keys()))<= len(c)//2: return len(list(d.keys()))
        return len(c)//2
        