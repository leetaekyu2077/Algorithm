class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int whole = brown + yellow;
        
        int cols;
        for (int i=3; i<=(int)Math.sqrt(whole); i++) {
            if (whole % i == 0) {
                cols = whole / i;
                if (((cols+i)*2 - 4) == brown) {
                    answer[0] = cols;
                    answer[1] = i;
                    break;
                }
            }
        }
        
        return answer;
    }
}