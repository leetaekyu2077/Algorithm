package boj1978;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] nums = new int[n];
        for (int i=0; i<n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(check(nums));        // 소수 판별 함수
        System.out.println(eratos(nums));       // 에라토스테네스의 체
    }

    private static int check(int[] nums) {
        int count = 0;
        boolean flag = false;

        for (int i=0; i<nums.length; i++) {
            flag = false;
            if (nums[i] != 1) {
                for (int j=2; j*j<=nums[i]; j++) {
                    if (nums[i] % j != 0) {
                        continue;
                    } else {
                        flag = true;
                        break;
                    }
                }
                if (!flag) count += 1;
            }
        }
        return count;
    }

    private static int eratos(int[] nums) {
        int count = 0;
        int[] a = new int[1000+1];
        int size = (int)Math.sqrt(1000)+1;
        a[1] = 1;

        for (int i=2; i<size; i++) {
            if (a[i] == 0) {
                for (int j=i*i; j<=1000; j+=i) {
                    a[j] = 1;
                }
            }
        }
        
        for (int i=0; i<nums.length; i++) {
            if (a[nums[i]] != 1)
                count += 1; 
        }

        return count;
    }
}
