import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        //useAscii(s);
        useHashMap(s);
    }

    private static void useAscii(String s) {
        float score = 0;
        char detail;

        score = 69 - (int)s.charAt(0);
        if (score > 0) {
            detail = s.charAt(1);
            if (detail == '+') {
                score += 0.3;
            }
            else if (detail == '-') {
                score -= 0.3;
            }
        }
        else {
            score = 0;
        }
        System.out.println(score);
    }

    // python에서 dict 같은 자료구존
    private static void useHashMap(String s) {
        HashMap<String, Double> score = new HashMap<String, Double>();
        score.put("A+", 4.3);
        score.put("A0", 4.0);
        score.put("A-", 3.7);
        score.put("B+", 4.3);
        score.put("B0", 4.3);
        score.put("B-", 4.3);
        score.put("C+", 4.3);
        score.put("C0", 4.3);
        score.put("C-", 4.3);
        score.put("D+", 4.3);
        score.put("D0", 4.3);
        score.put("D-", 4.3);
        score.put("F", 0.0);

        System.out.println(score.get(s));
    }
}