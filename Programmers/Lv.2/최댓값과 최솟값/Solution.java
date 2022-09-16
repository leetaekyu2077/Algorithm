class Solution {
    public String solution(String s) {
        String answer = "";
        String[] nums = s.split(" ");
        
        int max, min;
        max = min = Integer.parseInt(nums[0]);
        
        for (int i=1; i < nums.length; i++) {
            int temp = Integer.parseInt(nums[i]);
            
            if (max < temp) max = temp;
            if (min > temp) min = temp;
        }
        
        answer = Integer.toString(min) + ' ' + Integer.toString(max);
        return answer;
    }
}