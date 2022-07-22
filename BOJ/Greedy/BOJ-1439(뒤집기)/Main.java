import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        char[] arr = s.toCharArray();

        int zero = 0, one = 0;
        char prior = '2';

        for (char c : arr) {
            if (c != prior) {
                prior = c;
                if (c == '0') zero += 1;
                else if (c == '1') one += 1;
            }
        }
        System.out.println(Math.min(zero, one));
    }
}
