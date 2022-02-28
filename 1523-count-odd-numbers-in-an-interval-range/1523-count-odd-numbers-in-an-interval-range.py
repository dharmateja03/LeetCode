class Solution:
    def countOdds(self, l: int, h: int) -> int:
        if l%2==0:l+=1
        if h%2==0:h-=1
        return ((h-l)//2) +1
        