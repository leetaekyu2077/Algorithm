import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");
        
        int a = Integer.parseInt(nums[0]);
        int b = Integer.parseInt(nums[1]);

        int result1 = gcd(a, b); 
        int result2 = (a * b) / result1;

        System.out.print(Integer.toString(result1) + '\n' + Integer.toString(result2));
    }

    public static int gcd(int a, int b) {
        int big, small;
        int temp;

        if (a > b) {
            big = a;
            small = b;
        }
        else {
            big = b;
            small = a;
        }

        while (small > 0) {
            temp = small;
            small = big % small;
            big = temp;
        }
        return big;
    }
}
