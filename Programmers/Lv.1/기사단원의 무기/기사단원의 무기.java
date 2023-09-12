class Solution {
    public int solution(int number, int limit, int power) {
        
        int[] count = new int[number + 1];   
        
        // 일정 범위 내의 약수 구하기 테크닉
        for (int i = 1; i <= number; i++) {
            for (int j = 1; j <= number / i; j++) {
                count[i * j]++;
            }
        }
        
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            if (count[i] > limit) {
                answer += power;
            } else {
                answer += count[i];
            }
        }
        
        return answer;
    }
}