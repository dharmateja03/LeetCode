class Solution:
    def squareIsWhite(self, c: str) -> bool:
        s="0abcdefgh"
        a=s.index(c[0])
        if int(a)%2==0 and int(c[1])%2==0:
            return 0
        elif  int(a)%2!=0 and int(c[1])%2!=0 :
            return 0
        return 1