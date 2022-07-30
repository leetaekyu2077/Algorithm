package BOJ.boj4659;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String password;
        while (true) {
            password = br.readLine();  
            if (!password.equals("end")) {
                if (!hasVowel(password)) {
                    bw.write("<" + password + ">" + " is not acceptable.\n");
                    continue;
                }
                if (!consecutiveThree(password)) {
                    bw.write("<" + password + ">" + " is not acceptable.\n");
                    continue;
                }
                if (!sameDouble(password)) {
                    bw.write("<" + password + ">" + " is not acceptable.\n");
                    continue;
                }
                bw.write("<" + password + ">" + " is acceptable.\n");
            } else {
                break;
            }
        }
        bw.close();
    }

    public static boolean hasVowel(String password) {
        if (password.contains("a") || 
            password.contains("e") || 
            password.contains("i") || 
            password.contains("o") || 
            password.contains("u")) {
                return true;
        }
        else {
            return false;
        }
    }

    public static boolean consecutiveThree(String password) {
        String vowels = "aeiou";
        int count = 1;
        String temp;
        boolean current, prior;

        temp = String.valueOf(password.charAt(0));
        if (vowels.contains(temp)) {
            prior = true;
        } else {
            prior = false;
        }

        for (int i=1; i<password.length(); i++) {
            temp = String.valueOf(password.charAt(i));
            if (vowels.contains(temp)) {
                current = true;
            } else {
                current = false;
            }
            // 모음일 때
            if (prior && current) {
                count += 1;
                if (count == 3)
                    return false;
            }
            // 자음일 때
            else if (!prior && !current) {
                count += 1;
                if (count == 3)
                    return false;
            }
            else {
                count = 1;
                prior = current;
            }
        }
        return true;
    }

    public static boolean sameDouble(String password) {
        char prior = password.charAt(0);
        char current = ' ';
        for (int i=1; i<password.length(); i++) {
            current = password.charAt(i);
            if ((current == 'e' || current == 'o') || (prior != current)) {
                prior = current;
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
}