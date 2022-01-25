class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i=0
        a,b=0,0
        if len(arr)==1:
            return 0
        

        while(i+1<len(arr) and arr[i+1]-arr[i]>0):
            i+=1
            a=1
        if i == 0 or i == len(arr)-1:
            return False
        while(i+1<len(arr) and arr[i]-arr[i+1]>0):
            i+=1
            b=1
            
        if i==len(arr)-1 :
            return 1
        return 0
                
        
        