import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int c = br.read();  // read() 함수는 입력된 하나의 문자에 대응하는 아스키코드 숫자 반환
        System.out.println(c);
    }
}