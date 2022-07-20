import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n, k;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // br.readLine().split(" ") 보다 StringTokenizer가 빠름
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken()) - 1;

        int[] nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        // Arrays.sort(nums);           // Solution 1. sort 후, k번째 수 출력하기 - 성공
        quickSort(nums, 0, n-1);    // Solution 2. Quick Selection 사용 (중앙값 pivot 사용해야만 성공;;)
        System.out.println(nums[k]);
    }

    private static void quickSort(int[] arr, int left, int right) {
        
        if (left < right) {
            int pivot = partition(arr, left, right);
            // pivot 왼쪽에 있는 수는 정렬되있던 말던 pivot보다 작은 수들
            // 따라서 pivot에 위치한 값은 "전체에서 pivot + 1번째"로 큰 수라는 의미
            if (pivot == k) {
                return;
            } else if (pivot > k) {
                quickSort(arr, left, pivot - 1);
            } else {
                quickSort(arr, pivot + 1, right);
            }
        }
    }

    private static int partition(int[] arr, int left, int right) {
        if (left + 1 == right) {
            if (arr[left] > arr[right]) {
                swap(arr, left, right);
            }
            return right;
        }

        int mid = (left + right) / 2;
	    swap(arr, left, mid);   // 중앙값을 첫 번째 요소로 이동
	    int pivot = arr[left];
	    int i = left+1, j = right;

	    while (i <= j) {
		    while (pivot < arr[j] && j > 0) {
                j--;
            }
		    while (pivot > arr[i] && i < arr.length-1) {
                i++;
            }
            if (i <= j) {
                swap(arr, i++, j--);
            }
	    }
        arr[left] = arr[j];
        arr[j] = pivot;
        return j;
    }

    private static void swap(int[] arr, int a, int b) {
        int temp = arr[b];
        arr[b] = arr[a];
        arr[a] = temp;
    }
}
