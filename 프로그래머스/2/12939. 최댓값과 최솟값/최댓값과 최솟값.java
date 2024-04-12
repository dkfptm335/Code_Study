import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String[] numbers = s.split(" ");
        int[] intNumbers = Arrays.stream(numbers).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(intNumbers);
        return intNumbers[0] + " " + intNumbers[intNumbers.length - 1];
    }
}