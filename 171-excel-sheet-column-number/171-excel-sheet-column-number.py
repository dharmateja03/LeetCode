class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s)==1:
            return ord(s)+1-ord("A")
        else:
                res = 0
                for c in s:
                    res = res*26 + ord(c)-ord('A')+1
                return res
            
        