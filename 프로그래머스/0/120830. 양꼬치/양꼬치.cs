using System;

public class Solution {
    public int solution(int n, int k) {
        // n: 양꼬치
        // k: 음료수
        
        // n / 10 → 음료수 서비스 개수
        
        int answer = 0;
        
        answer = 12000 * n + 2000 * (k - (n/10));
        
        return answer;
    }
}