class Solution {
    public int solution(int[] array, int height) {
        int human = 0;
        for (int arr: array) {
            if (arr > height) {
                human++;
            }
        }
        return human;
    }
}