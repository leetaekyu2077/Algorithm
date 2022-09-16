class Solution {
    int answer = 0;
    
    public void dfs(int[] numbers, int target, int idx, int result) {
        if (idx == numbers.length-1) {
            if (result + numbers[idx] == target)
                answer += 1;
            else if (result - numbers[idx] == target)
                answer += 1;
        } else {
            dfs(numbers, target, idx+1, result + numbers[idx]);
            dfs(numbers, target, idx+1, result - numbers[idx]);
        }
    }
    
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        
        return answer;
    }
}