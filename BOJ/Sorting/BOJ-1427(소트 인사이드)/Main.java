package BOJ.boj1427;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        Integer[] nums = new Integer[s.length()];
        
        int n = Integer.parseInt(s);
        for (int i=0; i<nums.length; i++) {
            nums[i] = n % 10;
            n /= 10;
        }
        Arrays.sort(nums, Collections.reverseOrder());
        // regex 뜻 : 0~9를 제외하고 모든 문자 ""로 대체 
        System.out.println(Arrays.toString(nums).replaceAll("[^0-9]",""));
    }
}
