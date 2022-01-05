class Solution:
    def interpret(self, c: str) -> str:
        ans=""
        i=0
        while i<len(c):
            if c[i]=="G":
                ans+="G"
            elif c[i]=="(" and c[i+1]==")":
                ans+="o"
                i+=1
            elif c[i]!="(" :
                ans+="al"
                i+=2
            i+=1
        return ans
        