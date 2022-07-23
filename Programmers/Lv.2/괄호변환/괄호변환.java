package Programmers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 괄호변환 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String p = br.readLine();

        System.out.print(convert(p));
    }

    private static String convert(String p) {
        String result = "";
        int stk;
        char std;

        if (!isCorrect(p)) {
            std = p.charAt(0);
            stk = 1;
            String u = "", v = "";

            for (int i=1; i<p.length(); i++) {
                if (p.charAt(i) == std) {
                    stk += 1;
                } else {
                    stk -= 1;
                    if (stk == 0) {
                        u = p.substring(0, i+1);
                        v = p.substring(i+1);
                        break;
                    }
                }
            }

            if (isCorrect(u)) {
                result += u + convert(v);
            } else {
                result = "(" + convert(v) + ")";
                for (int i=1; i<u.length()-1; i++) {
                    if (u.charAt(i) == '(') {
                        result += ")";
                    } else {
                        result += "(";
                    }
                }
            }

        } else {
            result = p;
        }
        return result;
    }

    private static boolean isCorrect(String u) {
        if (u.length() > 0) {
            int stk = 0;
            for (int i=0; i<u.length(); i++) {
                if (u.charAt(i) == '(') 
                    stk += 1;
                else {
                    if (stk > 0) 
                        stk -= 1;
                    else 
                        return false;
                }
            }
            if (stk > 0)
                return false;
        } 
        return true;
    }
}
