import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = 0, sum2 = 0;
        
        List<Integer> q1 = new ArrayList<>();
        List<Integer> q2 = new ArrayList<>();
        
        for (int i=0; i<queue1.length; i++) {
            // queue1 리스트 변환 & 요소 총합
            q1.add(queue1[i]);
            sum1 += queue1[i];
            // queue2 리스트 변환 & 요소 총합
            q2.add(queue2[i]);
            sum2 += queue2[i];
        }
        
        // 두 큐의 원소의 합이 짝수일 때
        if ((sum1+sum2) % 2 == 0) {
            int popped;
            int idx1 = 0, idx2 = 0;
            
            // 두 큐의 합이 같아질 때까지
            while (sum1 != sum2) {
                if (sum1 < sum2) {
                    // ArrayList.remove()의 시간복잡도는 O(n)이므로 시간초과 발생
                    // 제거 대신 큐의 첫번째 요소 index를 1씩 증가시키는 방식 사용
                    popped = q2.get(idx2);
                    q1.add(popped);
                    sum1 += popped;
                    sum2 -= popped;
                    idx2 += 1;
                } else {
                    popped = q1.get(idx1);
                    q2.add(popped);
                    sum2 += popped;
                    sum1 -= popped;
                    idx1 += 1;
                }
                answer += 1;
                if (sum1 == 0 || sum2 == 0 || answer >= queue1.length*4) {
                    return -1;
                }
            }
            return answer;
        // 두 큐의 원소의 합이 홀수일 때
        } else {
            return -1;
        }
    }
}