import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        
        Stack<Integer> stk = new Stack<>();
        
        for (int i=0; i < numbers.length; i++) {
            while (stk.size() > 0 && numbers[stk.peek()] < numbers[i]) {
                answer[stk.pop()] = numbers[i];
            }
            stk.push(i);
        }
        
        return answer;  
    }   
}