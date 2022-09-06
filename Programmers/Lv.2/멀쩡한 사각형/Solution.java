class Solution {
    public long solution(int w, int h) {
        long x = 1, y = 1;
        long removed = 1;
        // double slope = (double)h / w;
        
        while (true) {
            // 기울기를 미리 나누어 slope*x와 y값을 비교하는 방법을 사용했으나,
            // 큰 수를 나누면서 double 타입 특성으로 인해 소숫점에서 오차가 발생하여 실패
            // 곱하기를 먼저하고 나누면 오차가 줄어든다는 것을 알아내서
            // 아래 방법처럼 반복적이지만 곱하기를 먼저하기 위해 매차례 다시 계산하는 방법을 도입하여 성공함.
            if ((double)h*x/w < y) {
                removed += 1;
                x += 1;
            } else if ((double)h*x/w > y) {
                removed += 1;
                y += 1;
            } 
            else {
                // int형인 w*h를 아래와 같이 long으로 캐스팅없이 계산하면 오버플로우 발생함 주의
                return (long)w*h - removed*w/x;
            }
        }
    }
}