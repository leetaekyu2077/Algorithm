package boj5597;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = new int[30];

        int temp;
        for (int i=0; i<28; i++) {
            temp = Integer.parseInt(br.readLine()) - 1;
            nums[temp] = 1;
        }

        for (int i=0; i<30; i++) {
            if (nums[i] == 1) {
                continue;
            }
            else {
                System.out.println(String.valueOf(i+1));
            }
        }
    }
}