class Solution:
    def reverseDegree(self, s: str) -> int:
        
        total = 0
        for i,c in enumerate(s):
            reverse=26-(ord(c)-ord('a'))
            position= i+1

            total+=reverse*position
        return total