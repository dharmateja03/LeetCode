class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=""
        for i in bin(n)[2:]:
            if i=="1":
                s+="0"
            else:
                s+="1"
        return int(s,2)