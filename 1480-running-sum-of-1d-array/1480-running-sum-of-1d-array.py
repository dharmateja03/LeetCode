class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        ans=0
        l.append(nums[0])
        for i in range(1,len(nums)):
            ans=l[i-1]+nums[i]
            l.append(ans)
        return l
            