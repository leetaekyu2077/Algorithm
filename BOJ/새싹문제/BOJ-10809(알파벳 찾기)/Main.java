import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = br.readLine();
        String alphabet = "abcdefghijklmnopqrstuvwxyz";

        int temp;
        for (int i=0; i<alphabet.length(); i++) {
            temp = s.indexOf(alphabet.charAt(i));
            bw.write(String.valueOf(temp) + " ");
        }
        bw.close();
    }
}
