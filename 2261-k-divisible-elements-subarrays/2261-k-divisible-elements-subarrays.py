class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        s=set()
        m= int(1e9+7)
        for i in range(len(nums)):
            cnt=0
            pwr= 17
            h=0
            for j in range(i,len(nums)):
                if nums[j]%p ==0:
                    cnt+=1
                    if cnt >k:
                        break
                
                h= h*pwr + nums[j]                
                pwr= (pwr*(17))%m
                s.add(h)
               
                
        return len(s)
                    
                    
        