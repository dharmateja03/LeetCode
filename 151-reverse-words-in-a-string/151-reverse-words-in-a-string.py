class Solution:
    def reverseWords(self, s: str) -> str:
       
        l=[i for i in s.split(" ") if len(i)>0]
        return " ".join(l[::-1]).strip()
        