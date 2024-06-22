function getGcd(a, b) {
    if (b == 0) {
        return a;
    }
    
    return getGcd(b, a % b);
}

function solution(numer1, denom1, numer2, denom2) {
    let answer = [];
    
    const numer = numer1 * denom2 + numer2 * denom1;
    const denom = denom1 * denom2;
    
    const gcd = getGcd(numer, denom);
    
    answer.push(numer / gcd, denom / gcd);
    return answer;
}