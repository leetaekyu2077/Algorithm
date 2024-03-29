class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;

        while ((a = (a + a%2)/2) != (b = (b + b%2)/2)) {
            answer++;
        }
        return answer;
    }
}

// 다른 사람이 푼 비트연산 답 : 이진수로 변환해서 XOR 연산한 결과의 길이
// 각각 -1을 하는 이유 : -1을 빼서 0부터 시작하는 이진수 연산에 맞게 바꿈.
// XOR 하는 이유 : 
// 두 수가 만나 겨뤄서 승부가 난다는 것 -> 두 수의 차이가 없어진다는 것 (둘 중 하나는 이겨서 다른 하나를 대체하게 되는 것이므로)
// 두 수의 차이가 클수록 나중에 만나게 됨. 그럼 얼마나 차이가 날 때 얼마나 나중이냐?
// 토너먼트는 라운드마다 전체가 2씩 나눠지며 줄어드므로, 두 수의 차이가 없어질 때까지 전체를 2로 나누는 횟수가 둘이 만나 겨루는 라운드 수!
// 두 수를 2진수로 변환한 후 비교했을 때, 값이 서로 다른 자릿수 중 가장 큰 자릿수의 자릿'수'만큼 나중에 만나게 됨. (2^(그 자릿수)만큼 차이가 난다는 뜻이므로 자릿수만큼 2를 나눠줘야 둘의 차이가 사라짐) 
// 따라서, 서로 다른 자릿수들을 얻기 위해 XOR을 취함 -> 나온 결과의 '길이'가 서로 다른 자릿수 중 가장 큰 자릿수의 자릿'수'가 되는 것
// ex) 100, 110은 2번째 자릿수가 다르므로, 2를 두 번은 나눠줘야 자리가 차이가 없어지게 됨.

// class Solution
// {
//     public int solution(int n, int a, int b)
//     {
//         return Integer.toBinaryString((a-1)^(b-1)).length();
//     }
// }