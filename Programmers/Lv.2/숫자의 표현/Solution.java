// class Solution {
//     public int solution(int n) {
//         int answer = 0;
//         int sum;
        
//         for (int i=1; i<=n; i++) {
//             sum = 0;
//             for (int j=i; sum<=n; j++) {
//                 if (sum != n) {
//                     sum += j;
//                 } else {
//                     answer++;
//                     break;
//                 }
//             }
//         }
        
//         return answer;
//     }
// }

// 정답 풀이
// https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9CLevel-2
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i=1; i<=n; i+=2) {
            if (n%i == 0)
                answer++;
        }
        
        return answer;
    }
}