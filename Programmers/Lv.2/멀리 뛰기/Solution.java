// dp[i] = dp[i-1] + dp[i-2] 인 이유
// 마지막에 1칸을 뛸 것인가 2칸을 뛸 것인가
// 1칸을 뛸 거면 i-1번째 케이스들에서 마지막에 1칸만 뛰면 됨. 2칸을 뛸 거면 i-2번째 케이스들에서 마지막에 2칸만 뛰면 됨.

class Solution {
    public int solution(int n) {
        int[] dp = new int[n+2];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i=3; i<=n; i++) {
            dp[i] = (dp[i-2] + dp[i-1]) % 1234567;
        }
        
        return dp[n];
    }
}