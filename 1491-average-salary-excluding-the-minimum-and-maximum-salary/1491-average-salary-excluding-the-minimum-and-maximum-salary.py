class Solution:
    def average(self, s: List[int]) -> float:
        return (sum(s)-max(s)-min(s))/(len(s)  -2)
        