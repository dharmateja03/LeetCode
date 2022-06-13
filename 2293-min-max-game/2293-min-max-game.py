class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            ans = []
            for i in range(0,len(nums),2):
                if (i//2)%2 == 0:
                    ans.append(min(nums[i],nums[i+1]))
                else:
                    ans.append(max(nums[i],nums[i+1]))
            nums = ans
        return nums[0]