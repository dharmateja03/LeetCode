class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        #nums = [4,1,2,3]
        ans=[]
        for i in range(len(nums)):
            if not i%2:e.append(nums[i])
            else:o.append(nums[i])
        e=sorted(e)
        o=sorted(o)
        o=o[::-1]
        for i in range(min(len(e),len(o))):
            ans.append(e[i])
            ans.append(o[i])
        if len(e)>len(o):ans.append(e[-1])
        elif len(o)>len(e):ans.append(o[-1])
        
        return ans