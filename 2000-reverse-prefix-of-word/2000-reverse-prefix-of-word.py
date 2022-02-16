class Solution:
    def reversePrefix(self, w: str, ch: str) -> str:
        if ch in w:
            a=w.index(ch)
            return w[:a+1][::-1]+w[a+1:]
        return w
        