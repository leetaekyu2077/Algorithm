package boj2309;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] dwerfs = new int[9];
        int sum = 0;

        for (int i=0; i<9; i++) {
            dwerfs[i]= sc.nextInt();
            sum += dwerfs[i];
        }
        Arrays.sort(dwerfs);

        // 자기 자신끼리의 중복을 제외하면서 조합하는 for문
        outer : for (int i=1; i<9; i++) {
            for (int j=0; j<i; j++) {
                if (sum - (dwerfs[i] + dwerfs[j]) == 100) {
                    for (int k=0; k<9; k++) {
                        if (k != i && k != j) {
                            System.out.println(dwerfs[k]);
                        }
                    }
                    break outer;
                }   
            }
        }
    }
}
