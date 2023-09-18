import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        
        HashMap<Character, Integer> nums = new HashMap<>();
        
        // X에 있는 숫자들의 갯수를 해시맵에 저장
        for (int i=0; i < X.length(); i++) {
            char curr = X.charAt(i);
            int value = 0;
            
            if (nums.containsKey(curr)) {
                value = nums.get(curr);
            }
            nums.put(curr, value+1);
        }
        
        List<Character> common = new ArrayList<>();
        
        // Y에 있는 숫자들을 보면서 겹치는 숫자를 기록
        for (int i=0; i<Y.length(); i++) {
            char curr = Y.charAt(i);
            int value;
            
            if (nums.containsKey(curr)) {
                value = nums.get(curr);
                if (value > 0) {
                    common.add(curr);
                }
                nums.put(curr, value - 1);
            }
            
        }
        
        if (common.size() == 0)
            return "-1";
        
        common.sort(Comparator.reverseOrder());
        if (common.get(0) == '0')
            return "0";
    
        StringBuilder sb = new StringBuilder();
        for (Character ch: common) {
            sb.append(ch);
        }
        
        return sb.toString();
    }
}