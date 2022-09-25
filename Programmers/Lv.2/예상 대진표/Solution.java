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