class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cp=0
        cn=0
        if nums.count(0):
            return 0
        else:
            for i in nums:
                if i>0:
                    continue
                else:
                    cp+=1
            if cp%2==0:
                return 1
            return -1
        