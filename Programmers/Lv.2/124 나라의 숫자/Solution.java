import java.lang.StringBuffer;

class Solution {
    public String solution(int n) {
        String answer = "";
        String[] nums = {"4", "1", "2"};
        
        int r;
        while (n != 0) {
            r = n % 3;
            n = n / 3;
            if (r == 0) n -= 1;
            answer += nums[r];
        }
        StringBuffer sb = new StringBuffer(answer);
        answer = sb.reverse().toString();
        return answer;
    }
}