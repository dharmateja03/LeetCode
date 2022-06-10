class Solution:
    def canBeEqual(self, t: List[int], a: List[int]) -> bool:
        
        return sorted(t)==sorted(a)