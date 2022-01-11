class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        s=""
        if len(arr)<3:
            return False
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]>0:
                s+="1"
            elif arr[i]-arr[i-1]<0:
                s+="0"
            elif arr[i-1]-arr[i]==0:
                return False
        if s[0]=="1" and len(s.strip("0").strip("1"))==0 and s[-1]=="0":
            return True
        return False
        