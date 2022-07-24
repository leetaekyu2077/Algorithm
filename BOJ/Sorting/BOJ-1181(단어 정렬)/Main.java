package BOJ.boj1181;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        Set<String> words = new HashSet<>();
        for (int i=0; i<n; i++) {
            words.add(br.readLine());
        }

        List<String> result = new ArrayList<String>(words);
        Collections.sort(result, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                int temp = s1.length() - s2.length();
                if (temp == 0) {
                    return s1.compareTo(s2);
                } else {
                    return temp;
                }
            }
        });

        for (int i=0; i<result.size(); i++) {
            bw.write(result.get(i) + "\n");
        }
        bw.close();
    }
}
