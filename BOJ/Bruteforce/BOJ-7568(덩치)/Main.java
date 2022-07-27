import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static class Person {
        int weight;
        int height;
        int rank = 1;
    }
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        Person[] people = new Person[n];
        for (int i=0; i<n; i++) {
            Person p = new Person();
            st = new StringTokenizer(br.readLine());
            p.weight = Integer.parseInt(st.nextToken());
            p.height = Integer.parseInt(st.nextToken());
            people[i] = p;
        }

        for (int i=1; i<n; i++) {
            for (int j=0; j<i; j++) {
                if (people[i].height > people[j].height && people[i].weight > people[j].weight) {
                    people[j].rank += 1;
                } 
                else if (people[i].height < people[j].height && people[i].weight < people[j].weight) {
                    people[i].rank += 1;
                }
            }
        }

        for (int i=0; i<n; i++) {
            bw.write(people[i].rank + " ");
        }
        bw.close();
    }
}
