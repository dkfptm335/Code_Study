import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 컴퓨터마다 6자리의 고유번호
        // 5자리에는 00000~99999까지의 숫자가 들어갈 수 있음
        // 6번째 자리에는 검증수, 앞 5자리의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

        // 1. 5자리의 숫자를 입력받는다.
        // 2. 각 자리의 숫자를 제곱한 수의 합을 구한다.
        // 3. 10으로 나눈 나머지를 구한다.
        // 4. 검증수를 출력한다.

        Scanner sc = new Scanner(System.in);
        int sum = 0;

        int[] arr = new int[5];
        for(int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i] * arr[i];
        }

        sc.close();

        System.out.println(sum % 10);

    }
}
