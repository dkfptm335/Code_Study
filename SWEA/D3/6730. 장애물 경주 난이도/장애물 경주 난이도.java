import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(reader.readLine());

        for (int i = 1; i <= t; i++) {
            int n = Integer.parseInt(reader.readLine());
            String[] strArray = reader.readLine().split(" ");
            int[] blockHeights = Arrays.stream(strArray).mapToInt(Integer::parseInt).toArray();

            int upMax = 0, downMax = 0;

            for (int j = 0; j < n - 1; j++) {
                int tmp;
                if (blockHeights[j] < blockHeights[j + 1]) {
                    tmp = blockHeights[j + 1] - blockHeights[j];
                    if (tmp > upMax) {
                        upMax = tmp;
                    }
                } else {
                    tmp = blockHeights[j] - blockHeights[j + 1];
                    if (tmp > downMax) {
                        downMax = tmp;
                    }
                }
            }

            System.out.println("#" + i + " " + upMax + " " + downMax);
        }
    }
}
