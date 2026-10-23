class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1,s2=set(nums1),set(nums2)

        result=[[],[]]

        for i in s1:
            if i not in s2:
                result[0].append(i)
        
        for i in s2:
            if  i not in s1:
                result[1].append(i)
        

        return result

