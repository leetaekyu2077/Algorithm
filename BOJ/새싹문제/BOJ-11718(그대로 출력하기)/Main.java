package boj11718;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s;
        
        // 입력 수가 정해지지 않을 때 여러 줄 입력 받는 방법
        while ((s = br.readLine()) != null) {
            bw.write(s+"\n");
        }
        bw.close();
    }
}
