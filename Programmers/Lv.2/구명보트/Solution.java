import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int head = 0, rear = people.length-1;
        
        Arrays.sort(people);
        while (head < rear) {
            if (people[head] + people[rear] <= limit) {
                answer += 1;
                head += 1;
                rear -=1;
            } else {
                rear -= 1;
                answer += 1;
            }
        }
        
        if (head <= rear) {
            answer += (rear-head) + 1;
        }
        
        return answer;
    }
}