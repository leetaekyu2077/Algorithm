package BOJ.boj13305;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int n = Integer.parseInt(br.readLine());
        int[] roads = new int[n-1];
        int[] cities = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n-1; i++) {
            roads[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            cities[i] = Integer.parseInt(st.nextToken());
        }

        // int 최댓값 넘어가서 long으로 선언
        long price = cities[0];
        long total_cost = 0;

        for (int i=0; i<n-1; i++) {
            if (price > cities[i]) {
                price = cities[i];
            }
            // 피연산자 둘 다 int이면, 계산 결과가 int 최댓값을 넘어갈 때 overflow 발생. 둘 중 하나는 long이어야 함.
            total_cost += price * roads[i];
        }

        System.out.println(total_cost);
    }
}
