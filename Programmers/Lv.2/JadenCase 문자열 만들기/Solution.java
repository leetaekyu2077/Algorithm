// 처음, 중간, 끝 공백과 연속 공백 모두 살린 채로 
// JadenCase 조건에 만족하는 문자열을 만들어야 함!

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] word_list = s.toLowerCase().split(" ", -1);    //split() 함수에 두 번째 인자 limit에 음수를 주면, 맨 마지막 값도 생략없이 추가
        
        for (String word: word_list) {
            if (word.length() > 0) {
                answer += word.substring(0, 1).toUpperCase() + word.substring(1) + " ";
            } else {
                answer += " ";
            }
        } 
        
        if (answer.length() > 0) {
            answer = answer.substring(0, answer.length()-1);
        }
        
        return answer;
    }
}