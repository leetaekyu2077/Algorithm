class 덧칠하기 {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int idx = 0;
        int end;
        
        while (idx < section.length) {
            answer += 1;
            end = section[idx]+m-1;
            idx += 1;
            
            while (idx < section.length && section[idx] <= end) {
                idx += 1;
            }
        }

        return answer;
    }
}