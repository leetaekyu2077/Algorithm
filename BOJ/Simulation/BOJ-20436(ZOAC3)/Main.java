package BOJ.boj20436;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static class Location {
        int r, c;
        Location(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String[] qwerty = { "qwertyuiop", "asdfghjkl", "zxcvbnm"};
        HashMap<Character, Location> keyboard = new HashMap<>();

        for (int i=0; i<qwerty.length; i++) {
            for (int j=0; j<qwerty[i].length(); j++) {
                Location temp = new Location(i, j);
                keyboard.put(qwerty[i].charAt(j), temp);
            }
        }

        st = new StringTokenizer(br.readLine());
        char l = st.nextToken().charAt(0);
        char r = st.nextToken().charAt(0);

        Location left = keyboard.get(l);
        Location right = keyboard.get(r);

        String input = br.readLine();
        int moved = 0;
        for (int i=0; i<input.length(); i++) {
            Location key_location = keyboard.get(input.charAt(i));
            if (key_location.c < 5 && input.charAt(i) != 'b') {
                moved += Math.abs(left.r - key_location.r) + Math.abs(left.c - key_location.c) + 1;
                left = key_location;
            } else {
                moved += Math.abs(right.r - key_location.r) + Math.abs(right.c - key_location.c) + 1;
                right = key_location;
            }
        }
        System.out.println(moved);
    }
}