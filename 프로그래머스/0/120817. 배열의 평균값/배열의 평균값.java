class Solution {
    public double solution(int[] numbers) {
        int sum = 0;
        double avg = 0.0;
        
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        
        avg = (double) sum / numbers.length;
        
        return avg;
    }
}