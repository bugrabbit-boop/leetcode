class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int n= nums.length;
        int count =0;
         int maxcount=0;
        for(int j=0;j<n;j++){
            if(nums[j]==1){
                count++;
            }else{
                maxcount=Math.max(count,maxcount);
                count =0;
            }
        } 
        maxcount = Math.max(count,maxcount);  
    
        
        return maxcount;
    }
}