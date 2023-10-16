import java.util.*;

class 바탕화면정리 {
    public int[] solution(String[] wallpaper) {
        int row = wallpaper.length;
        int col = wallpaper[0].length();

        int[] answer = {row+1, col+1, -1, -1};
        for (int i=0; i<row; i++) {

            boolean flag = false;
            for (int j=0; j<col; j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    flag = true;
                    if (j < answer[1]) {
                        answer[1] = j;
                    }
                    if (j > answer[3]) {
                        answer[3] = j;
                    }
                }
            }

            if (flag) {
                if (i < answer[0]) {
                    answer[0] = i;
                }
                if (i > answer[2]) {
                    answer[2] = i;
                }
            }
        }

        answer[2] += 1;
        answer[3] += 1;
        return answer;
    }
}
