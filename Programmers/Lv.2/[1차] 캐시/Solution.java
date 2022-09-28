import java.util.Map;
import java.util.LinkedHashMap;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Map<String, String> cache = new LinkedHashMap<>(cacheSize, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > cacheSize;
            }
        };
        
        String name;
        for (String city : cities) {
            name = city.toUpperCase();
            if (cache.get(name) == null) {
                answer += 5;
                cache.put(name, "");
            } else
                answer += 1;
        }
        return answer;
    }
}