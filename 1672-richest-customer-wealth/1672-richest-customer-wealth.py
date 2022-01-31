class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        ans=0
        for i in a:
            ans=max(ans,sum(i))
        return ans
        