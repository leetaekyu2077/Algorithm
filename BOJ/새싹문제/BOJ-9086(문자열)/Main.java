import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        String s;
        
        for(int i=0; i<t; i++) {
            s = br.readLine();
            System.out.println(String.valueOf(s.charAt(0)) + String.valueOf(s.charAt(s.length()-1)));
        }
    }
}
