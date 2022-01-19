class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        mx,s=-11111111111111,0
        for i in a:
            s+=i
            mx=max(mx,s)
            if s<0:
                s=0
        return mx
            
        
        