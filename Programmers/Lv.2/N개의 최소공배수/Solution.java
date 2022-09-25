class Solution {
    public int gcd(int a, int b) {
        int temp;
        while (b > 0) {
            a = a%b;
            temp = a;
            a = b;
            b = temp;
        }
        return a;
    }
    
    public int solution(int[] arr) {
        int gcd = 0;
        
        for (int i=0; i<arr.length-1; i++) {
            gcd = gcd(arr[i], arr[i+1]);
            arr[i+1] = (arr[i] * arr[i+1]) / gcd; 
        }
        return arr[arr.length-1];
    }
}