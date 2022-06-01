class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r=0
        for i in range(1<<len(nums)):
            s=0
            for j in range(len(nums)):
                if ((i & (1<<j))):
                    s^= nums[j]
            r+=s
        return r
                    
        