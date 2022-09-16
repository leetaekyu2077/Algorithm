import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};

        List<String> used = new ArrayList<>();
        used.add(words[0]);
        char last = words[0].charAt(words[0].length()-1);
        
        int i;
        for (i=1; i<words.length; i++) {
            String temp = words[i];

            if (used.contains(temp))
                break;
            if (last != temp.charAt(0)) 
                break;
            
            used.add(temp);
            last = temp.charAt(temp.length()-1);
        }
        
        if (i < words.length) {
            System.out.println(i);
            answer[1] = i/n+1;
            answer[0] = i%n+1;
        }
        return answer;
    }
}
