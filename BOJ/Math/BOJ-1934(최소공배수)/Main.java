import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i=0; i < t; i++) {
            String[] nums = br.readLine().split(" ");
            int a = Integer.parseInt(nums[0]);
            int b = Integer.parseInt(nums[1]);

            if (a > b) {
                System.out.println((a*b) / gcd(a, b));
            }
            else {
                System.out.println((a*b) / gcd(b, a));
            }
        }
    }

    static int gcd(int a, int b) {
        int temp = 0;
        while (b > 0) {
            temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}