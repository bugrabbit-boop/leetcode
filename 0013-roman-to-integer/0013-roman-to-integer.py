class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        dicto={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}   

        for a,b in zip(s,s[1:]):
            if dicto[a] < dicto[b]:
                res-=dicto[a]
            else:
                res+=dicto[a]

        return res+dicto[s[-1]]    