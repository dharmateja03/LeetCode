class Solution:
    def twoSum(self, l: List[int], target: int) -> List[int]:
        low=0
        h=len(l)-1
        while(low<=h):
            if l[low]+l[h]==target:
                return [low+1,h+1]
            elif l[low]+l[h]>target:
                h-=1
            else:
                low+=1
        