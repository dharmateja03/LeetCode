class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums.index(min(nums)) + 1
        y = nums.index(max(nums)) + 1
        
        res = min(max(n-x+1, n-y+1) , max(x,y))       #minimum of going from right and going from left
        if x > y:  #exchange if needed so as to do one operation later assuming x is the smaller index
            x, y = y, x
        
        option = x + (n - y) + 1 #going left for smaller and right for larger
        res = min(res, option)
        
        return res if n > 2 else n