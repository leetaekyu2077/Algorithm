import java.util.Arrays;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        Arrays.sort(A);
        Arrays.sort(B);
        
        int idx_A = 0, idx_B = B.length-1;
        for (int i=0; i<A.length; i++) {
            answer += A[idx_A] * B[idx_B];
            idx_A++;
            idx_B--;
        }
        
        return answer;
    }
}