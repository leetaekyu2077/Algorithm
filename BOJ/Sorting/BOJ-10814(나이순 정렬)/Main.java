package BOJ.boj10814;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

// 이렇게 아예 Main class 밖으로 빼거나, Main class 내부에 있되 static 붙여야 함
class User {
    int age, order;
    String name;
    User(int age, int order, String name) {
        this.age = age;
        this.order = order;
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        User[] list = new User[n];

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            list[i] = new User(Integer.parseInt(st.nextToken()), i, st.nextToken());
        }
        Arrays.sort(list, (first, second) -> {
            if (first.age != second.age) {
                return first.age - second.age;
            } else {
                return first.order - second.order;
            }
        });

        for (int i=0; i<n; i++) {
            bw.write(Integer.toString(list[i].age) + " " + list[i].name + "\n");
        }
        bw.close();
    }  
}
