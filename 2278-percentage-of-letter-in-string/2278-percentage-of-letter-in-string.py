class Solution:
    def percentageLetter(self, s: str, l: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        #print(d[l])
        if l in s:
            return (d[l]*100)//len(s)
        else:
            return 0