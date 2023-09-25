import java.util.*;

class Solution {

    public Integer[] solution(String today, String[] terms, String[] privacies) {

        List<Integer> answer = new ArrayList<>();

        // 각 term이 저장된 hash map 생성
        HashMap<String, Integer> periodMap = new HashMap<>();
        for (String term: terms) {
            String[] temp = term.split(" ");
            periodMap.put(temp[0], Integer.parseInt(temp[1]));
        }

        int current = convertToDay(today);
        for (int i=0; i < privacies.length; i++) {
            String[] temp = privacies[i].split(" ");

            int period = periodMap.get(temp[1]);
            if (convertToDay(temp[0]) + period*28 <= current) {
                answer.add(i+1);
            }
        }

        return answer.toArray(new Integer[answer.size()]);
    }

    private int convertToDay(String date) {

        String[] splitDate = date.split("\\.");

        int year = Integer.parseInt(splitDate[0]) * 28 * 12;
        int month = Integer.parseInt(splitDate[1]) * 28;
        int day = Integer.parseInt(splitDate[2]);

        return year + month + day;
    }
}