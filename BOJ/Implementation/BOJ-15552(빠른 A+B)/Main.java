import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        String[] nums;
        for (int i=0; i<t; i++) {
            nums = br.readLine().split(" ");
            bw.write(Integer.parseInt(nums[0])+Integer.parseInt(nums[1])+"\n");
        }
        bw.close();
    }
}