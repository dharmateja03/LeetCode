class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if t-nums[i] in d:
                return [i,d[t-nums[i]]]
            else:
                d[nums[i]]=i
        
       