class Solution:
    def firstPalindrome(self, w: List[str]) -> str:
        for i in w:
            if i==i[::-1]: return i
        return ""
        