package BOJ.boj1436;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int count = 1, title = 666;

        while (count != n) {
            title += 1;
            if (Integer.toString(title).contains("666")) {
                count += 1;
            }
        }
        System.out.println(title);
    }
}
