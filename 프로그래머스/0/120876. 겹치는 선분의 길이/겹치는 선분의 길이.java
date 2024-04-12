class Solution {
    public int solution(int[][] lines) {
        int startMin = Integer.MAX_VALUE;
        int endMax = Integer.MIN_VALUE;
        for (int[] line : lines) {
            startMin = Math.min(startMin, line[0]);
            endMax = Math.max(endMax, line[1]);
        }

        int[] count = new int[endMax - startMin + 1];

        for (int[] line : lines) {
            for (int i = line[0]; i < line[1]; i++) {
                count[i - startMin]++;
            }
        }

        int answer = 0;
        for (int value : count) {
            if (value > 1) {
                answer++;
            }
        }
        
        return answer;
    }
}