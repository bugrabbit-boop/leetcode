class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        curr=0
        max_alt=0

        for i in gain:
            curr+=i

            max_alt=max(max_alt,curr)
        return max_alt
    