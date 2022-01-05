class Solution:
    def interpret(self, c: str) -> str:
         return c.replace('()','o').replace('(al)','al')