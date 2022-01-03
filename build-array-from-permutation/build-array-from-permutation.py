class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        for i in range(len(nums)):
            l[i]=nums[nums[i]]
        return l
        