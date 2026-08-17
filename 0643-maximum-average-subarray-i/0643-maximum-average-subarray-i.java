class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n= nums.length;
        int  sum=0;
       
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
         double avg = (double)sum/k;
            for(int j=1;j<=n-k;j++){
               sum =sum-nums[j-1]+nums[j+k-1];
               avg=Math.max(avg,(double)sum/k);
            
            }

            return avg;
        }
    }

