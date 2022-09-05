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

// 채점 후 다른 사람 풀이 보고 수정한 코드 
// (왜 answer를 저렇게 붙일 생각을 안 했을까)

// class Solution {
//     public String solution(int n) {
//         String answer = "";
//         String[] nums = {"4", "1", "2"};
        
//         while (n != 0) {
//             answer = nums[n%3] + answer;
//             n = (n-1) / 3;
//         }
//         return answer;
//     }
// }