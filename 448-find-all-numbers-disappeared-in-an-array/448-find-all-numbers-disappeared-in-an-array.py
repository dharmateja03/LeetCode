class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = [0] + nums
        for i in range(len(nums)):
            
            nums[abs(nums[i])] = -abs(nums[abs(nums[i])])
        
        return [i for i in range(len(nums)) if nums[i] > 0]
        
        
        