class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = firstEl(nums,target);
        int last = lastEl(nums,target);

        return new int[]{first,last};
    }
        
       private int firstEl(int[] nums,int target){
        int left =0,right=nums.length-1;
        int  mid;
        int pos =-1;
        while(left<=right){
            mid=(left+right)/2;
            
            if(nums[mid]==target){
                pos =mid;
                right=mid-1;
            }
            
            else if (nums[mid]>target){
                right=mid-1;
            }else{
                left=mid+1;
            }
        }
        return pos;
    }
     private int lastEl(int[] nums,int target){
        int left =0,right=nums.length-1;
        int  mid;
        int pos =-1;
        while(left<=right){
            mid=(left+right)/2;
            
            if(nums[mid]==target){
                pos =mid;
                left=mid+1;
            }
            
            else if (nums[mid]>target){
                right=mid-1;
            }else{
                left=mid+1;
            }
        }
        return pos;
    }

    
}