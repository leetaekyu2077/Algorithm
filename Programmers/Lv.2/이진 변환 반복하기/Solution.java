class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        int len = 0, temp = 0, convert = 0;
        while (!s.equals("1")) {
            convert += 1;
            temp = s.length();
            s = s.replaceAll("0", "");
            len += temp - s.length();   // 0 제거 전과 후 문자열 길이 비교를 통해 0 갯수 도출
            
            s = Integer.toBinaryString(s.length());
        }
        
        answer[0] = convert;
        answer[1] = len;
        return answer;
    }
}