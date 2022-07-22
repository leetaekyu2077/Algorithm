import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int e, s, m;
        e = Integer.parseInt(st.nextToken()) % 15;
        s = Integer.parseInt(st.nextToken()) % 28;
        m = Integer.parseInt(st.nextToken()) % 19;

        int year = 1;
        while (true) {
            if (year % 15 == e && year % 28 == s && year % 19 == m)
                break;
            else
                year += 1; 
        }
        System.out.println(year);
    }
}