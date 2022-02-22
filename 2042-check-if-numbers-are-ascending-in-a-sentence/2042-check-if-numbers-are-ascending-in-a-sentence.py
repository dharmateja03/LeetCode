class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        for i in s.split(" "):
            if i.isnumeric():
                l.append(i)
        l=list(map(int,l))
        if len(l)== len(set(l)) and l==sorted(l):
            return 1
        return 0
        