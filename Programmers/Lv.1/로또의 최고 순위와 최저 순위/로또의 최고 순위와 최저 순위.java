import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {6, 6};
        boolean[] nums = new boolean[46];
        
        for (int num: win_nums) {
            nums[num] = true;
        }
        
        int common = 0;
        int zero = 0;
        for (int num: lottos) {
            if (num == 0)
                zero += 1;
            else if (nums[num]) {
                common += 1;
            }
        }
        
        if (common+zero > 1) 
            answer[0] = 7-(common+zero);
        if (common > 1)
            answer[1] = 7-common;
        
        return answer;
    }
}