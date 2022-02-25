class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1=list(map(int,v1.split(".")))
        v2=list(map(int,v2.split(".")))
        if len(v1)>len(v2):
            v2=v2+ ([0] * (len(v1)-len(v2)))
        elif len(v2)>len(v1):
            v1=v1+ ([0] * (len(v2)-len(v1)))
        if v1>v2:return 1
        elif v2>v1:return -1
        return 0
        