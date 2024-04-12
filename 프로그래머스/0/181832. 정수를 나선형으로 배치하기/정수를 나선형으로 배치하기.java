class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        // 배열 0으로 초기화
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer[i][j] = 0;
            }
        }

        int x = 0, y = 0, num = 1;
        String direction = "R";

        for (int i = 1; i <= n * n; i++) {
            answer[x][y] = num++;
            if (direction.equals("R")) {
                if (y + 1 < n && answer[x][y + 1] == 0) {
                    y++;
                } else {
                    direction = "D";
                    x++;
                }
            } else if (direction.equals("D")) {
                if (x + 1 < n && answer[x + 1][y] == 0) {
                    x++;
                } else {
                    direction = "L";
                    y--;
                }
            } else if (direction.equals("L")) {
                if (y - 1 >= 0 && answer[x][y - 1] == 0) {
                    y--;
                } else {
                    direction = "U";
                    x--;
                }
            } else if (direction.equals("U")) {
                if (x - 1 >= 0 && answer[x - 1][y] == 0) {
                    x--;
                } else {
                    direction = "R";
                    y++;
                }
            }
        }
        
        return answer;
    }
}