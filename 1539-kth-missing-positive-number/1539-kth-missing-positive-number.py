class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left,right=0,len(arr)
        arr1=[]
        while left < right:
            mid=(left+right)//2
            if arr[mid] - mid -1 < k:
                left=mid+1
            else:
                right=mid
        return right+k