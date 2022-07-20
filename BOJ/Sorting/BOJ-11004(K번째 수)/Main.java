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


        // Arrays.sort(nums);           //sort 후, k번째 수 출력하기 - 성공
        quickSort(nums, 0, n-1);    //Quick Selection 사용 - 93%에서 계속 시간초과 나서 포기
        System.out.println(nums[k]);
    }

    private static void quickSort(int[] arr, int left, int right) {
        if (left >= right) {
            return;
        }
        
        int pivot = partition(arr, left, right);
        // pivot 왼쪽에 있는 수는 정렬되있던 말던 pivot보다 작은 수들
        // 따라서 pivot에 위치한 값은 "전체에서 pivot + 1번째"로 큰 수라는 의미
        if (pivot > k) 
            quickSort(arr, left, pivot - 1);
        else if (pivot < k) 
            quickSort(arr, pivot + 1, right);
        else 
            return;
    }

    private static int partition(int[] arr, int left, int right) {
        int mid = (left + right) / 2;
	    swap(arr, left, mid);

	    int pivot = arr[left];
	    int temp = left;

	    while (left < right) {
		    while (pivot < arr[right] && left < right) {
                right--;
            }
		    while (pivot >= arr[left] && left < right) {
                left++;
            }
		    swap(arr, left, right);
	    }
        swap(arr, left, temp);
        return left;
    }

    private static void swap(int[] arr, int a, int b) {
        int temp = arr[b];
        arr[b] = arr[a];
        arr[a] = temp;
    }
}
