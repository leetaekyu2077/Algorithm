import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        
        int mid = str.length() / 2;

        if (sum(str.substring(0, mid)) == sum(str.substring(mid))) {
            System.out.println("LUCKY");
        } else {
            System.out.println("READY");
        }
    }

    static int sum(String str) {
        int result = 0;
        String[] list = str.split("");

        for (String s : list) {
            result += Integer.parseInt(s);
        }
        return result;
    }
}