package BOJ.boj1018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static String[] board1 = { "BWBWBWBW", 
                            "WBWBWBWB",
                            "BWBWBWBW", 
                            "WBWBWBWB",
                            "BWBWBWBW", 
                            "WBWBWBWB",
                            "BWBWBWBW", 
                            "WBWBWBWB"};
    static String[] board2 = { "WBWBWBWB",
                            "BWBWBWBW", 
                            "WBWBWBWB",
                            "BWBWBWBW", 
                            "WBWBWBWB",
                            "BWBWBWBW", 
                            "WBWBWBWB",
                            "BWBWBWBW"};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n, m;
                            
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        String[] input = new String[n];
        for (int i=0; i<n; i++) {
            input[i] = br.readLine();
        }

        int min = 2501;
        int temp;
        for (int i=0; i <= n-8; i++) {
            for (int j=0; j <= m-8; j++) {
                temp = minCount(input, i, j);
                if (min > temp) {
                    min = temp;
                }
            }
        }
        
        System.out.println(min);
    }

    public static int minCount(String[] input, int start_row, int start_col) {
        int min = 0;
        int count = 0;
        for (int i=0; i<8; i++) {
            for (int j=0; j<8; j++) {
                if (input[i+start_row].charAt(j+start_col) != board1[i].charAt(j)) {
                    count++;
                }
            }
        }
        min = count;
        count = 0;
        for (int i=0; i<8; i++) {
            for (int j=0; j<8; j++) {
                if (input[i+start_row].charAt(j+start_col) != board2[i].charAt(j)) {
                    count++;
                }
            }
        }

        if (min > count) 
            return count;
        else
            return min;
    }
}