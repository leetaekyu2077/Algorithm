package boj10807;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;     
        // String[] nums;       

        int n, x, count = 0;
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());     // StringTokenizer 사용
        // nums = br.readLine().split(" ");         // 배열 사용
        x = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            if (Integer.parseInt(st.nextToken()) == x) {
                count += 1;
            }
            // if (Integer.parseInt(nums[i]) == x) { 
            //     count += 1;
            // }
        }
        bw.write(String.valueOf(count));
        bw.close();
    }
}