class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int stack = 0;
        
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack++;
            } else {
                if (stack > 0)
                    stack--;
                else
                    return false;
            }
        }
        
        if (stack > 0)
            answer = false;

        return answer;
    }
}