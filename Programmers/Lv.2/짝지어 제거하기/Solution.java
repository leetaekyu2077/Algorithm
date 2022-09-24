import java.util.*;

class Solution
{
    public int solution(String s)
    {
        if (s.length() % 2 != 0)
            return 0;
        
        // Stack을 String 타입으로 선언 & s.split("") 으로 String 배열 만들어서 
        // String 타입끼리 비교하도록 풀어봤으나, String 타입은 여러모로 느림. 
        // 추후 다른 문제에서는 형변환 해주더라도 Character 쓰는 게 훠얼씬 빠를 듯.

        int answer = 0;
        Stack<Character> stk = new Stack<>();   
        stk.push('A');
        
        char item;
        for (int i=0; i<s.length(); i++) {
            item = s.charAt(i);
            if (stk.peek() == item) {
                stk.pop();
            } else {
                stk.push(item);
            }
        }
        
        if (stk.size() == 1)
            answer = 1;
        
        return answer;
    }
}