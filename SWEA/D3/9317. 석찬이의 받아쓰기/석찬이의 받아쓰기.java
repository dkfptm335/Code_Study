import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 테스트 케이스 개수
        int t = sc.nextInt();

        for (int i = 1; i <= t; i++) {
            // 문자열의 길이
            int n = sc.nextInt();
            // 문자열 2개 입력받기
            sc.nextLine();
            String origin = sc.nextLine();
            String[] originArr = origin.split("");

            String copy = sc.nextLine();
            String[] copyArr = copy.split("");

            int correct = 0;

            if (origin.equals(copy)) {
                correct = n;
            } else {
                for (int j = 0; j < n; j++) {
                    if (originArr[j].equals(copyArr[j])) {
                        correct++;
                    }
                }
            }

            System.out.printf("#%d %d", i, correct);
            System.out.println();
        }

        sc.close();
    }
}
