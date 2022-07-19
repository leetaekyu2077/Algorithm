package boj2738;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n, m;
        String[] temp;

        temp = br.readLine().split(" ");
        n = Integer.parseInt(temp[0]);
        m = Integer.parseInt(temp[1]);

        int[][] nums = new int[n][m];

        for (int i=0; i<n; i++) {
            temp = br.readLine().split(" ");
            for (int j=0; j<m; j++) {
                nums[i][j] = Integer.parseInt(temp[j]);
            }
        }
        for (int i=0; i<n; i++) {
            temp = br.readLine().split(" ");
            for (int j=0; j<m; j++) {
                nums[i][j] += Integer.parseInt(temp[j]);
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                bw.write(String.valueOf(nums[i][j]) + " ");
            }
            bw.write("\n");
        }
        bw.close();
    }
}
