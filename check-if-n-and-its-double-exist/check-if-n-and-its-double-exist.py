class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if (2*i in arr or i/2 in arr) and i!=0 :
                return True
            if 0 in arr and arr.count(0)==2:
                return True
        return False
        
        