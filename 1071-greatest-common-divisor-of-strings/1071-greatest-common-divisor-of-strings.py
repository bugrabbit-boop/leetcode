class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def isDivisible(long_str,sub_str):
            count=len(long_str)//len(sub_str)

            temp=""
            for i in range(count):
                temp+=sub_str
            
            if temp == long_str:
                return True
            return False
        
        if len(str1) < len(str2):
            short_str=str1
        else:
            short_str=str2
        
        for i in range(len(short_str),0,-1):
            part=short_str[:i]


            if isDivisible(str1,part) and isDivisible(str2,part):
                return part
        return ""
        
