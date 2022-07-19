package boj2475;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int temp = 0, sum = 0;

        for (int i=0; i<5; i++) {
            temp = sc.nextInt();
            sum += temp*temp;
        }
        System.out.println(sum % 10);
    }
}
