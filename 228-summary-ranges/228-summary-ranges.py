class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges,r=[],[]
        for n in nums:
            if n-1 not in nums:
                r=[]
                ranges+=r,
            r[1:]=n,
        return ['->'.join(map(str, r)) for r in ranges]
            
        