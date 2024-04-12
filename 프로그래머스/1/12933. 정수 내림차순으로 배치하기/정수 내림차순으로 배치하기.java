import java.util.Arrays;

class Solution {
    public long solution(long n) {
        // long to String
        String str = Long.toString(n);
        // String to char array
        char[] arr = str.toCharArray();
        // sort char array
        Arrays.sort(arr);
        // reverse char array
        StringBuilder sb = new StringBuilder(new String(arr));
        sb.reverse();
        // String to long
        return Long.parseLong(sb.toString());
    }
}