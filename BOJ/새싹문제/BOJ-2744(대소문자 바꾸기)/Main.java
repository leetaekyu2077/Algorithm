package boj2744;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        int temp;
        String result = "";
        for (int i=0; i<s.length(); i++) {
            temp = s.charAt(i);
            // 아스키 코드 상 대문자 범위 내일 때
            if (temp >= 65 && temp <= 90) {

                result += String.valueOf((char)temp).toLowerCase();
            }
            // 아스키 코드 상 소문자 범위 내일 때
            else if (temp >= 97 && temp <= 122) {
                result += String.valueOf((char)temp).toUpperCase();
            }
        }
        System.out.println(result);
    }
}