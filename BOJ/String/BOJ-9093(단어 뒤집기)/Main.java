import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        String[] lst;
        StringBuffer sb;
        for (int i=0; i < t; i++) {
            lst = br.readLine().split(" ");
            String result = "";
            for (String word : lst) {
                sb = new StringBuffer(" " + word);
                result += sb.reverse().toString();
            }
            System.out.println(result);
        }
    }
}