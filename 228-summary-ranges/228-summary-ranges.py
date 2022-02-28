class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges=[]
        for n in nums:
            if not ranges or ranges[-1][-1]+1<n   :
                ranges+=[],
            ranges[-1][1:]=n,
        return ['->'.join(map(str, r)) for r in ranges]
        