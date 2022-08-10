package BOJ.boj11399;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] times = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            times[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(times);

        int sum = 0;
        for (int i=1; i<=n; i++) {
            for (int j=0; j<i; j++) {
                sum += times[j];
            }
        }
        System.out.println(sum);
    }
}
