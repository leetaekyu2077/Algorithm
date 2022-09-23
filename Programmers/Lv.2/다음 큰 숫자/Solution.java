class Solution {
    public int solution(int n) {

        int ones = Integer.bitCount(n);
        
        while (true) {
            if (Integer.bitCount(++n) == ones)
                break;
        }
        
        return n;
    }
}