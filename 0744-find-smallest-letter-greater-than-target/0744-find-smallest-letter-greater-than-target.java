class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
     int left =0;
     int right = letters.length-1;
     int mid;
     int pos=-1;
     while(left<=right){
        mid=(left+right)/2;
        if(letters[mid] > target){
              pos=mid;
              right=mid-1;
        }else{
            left=mid+1;
        }
     }
     return pos == -1? letters[0]:letters[pos];
    }
}