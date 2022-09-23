class Solution {
    int[] records = new int[100001];
    
    public int fibo(int n) {
        int temp;
        
        if (n == 0)
            return 0;
        else if (n == 1)
            return 1;
        else {
            if (records[n] == 0) {
                temp = (fibo(n-1) + fibo(n-2))%1234567;
                records[n] = temp;
                return temp;
            } else {
                return records[n];
            }
        }
    }
    
    public int solution(int n) {
        int answer = 0;
        
        answer = fibo(n);
        return answer;
    }
}