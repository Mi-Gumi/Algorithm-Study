# [Silver I] 쉬운 계단 수 - 10844 

[문제 링크](https://www.acmicpc.net/problem/10844) 

### 성능 요약

메모리: 17752 KB, 시간: 208 ms

### 분류

다이나믹 프로그래밍

### 문제 설명

<p>45656이란 수를 보자.</p>

<p>이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.</p>

<p>N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.</p>

---

### Solution
#### python
```python
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        
        else:
            dp[i][j] = dp[i-1][j-1] +dp[i-1][j+1]

print(sum(dp[N]) % int(1e9))
```

#### Java
```java
import java.util.Scanner;

public class Main {
	static long div = 1000000000;
	static long sum = 0;
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[][] dp = new long[N+1][10];
		
		for (int i = 1; i < 10; i++) {
			dp[1][i] = 1;
		}
		
		for (int i = 2; i < N+1; i++) {
			for (int j = 0; j < 10; j++) {
				if (j==0) {
					dp[i][j] = dp[i-1][1] % div;
				}
				else if (j==9) {
					dp[i][j] = dp[i-1][8] % div;
				}
				else {
					dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % div;
				}				
			}
		}
		for (int i = 0; i < 10; i++) {
			 sum += dp[N][i];
		}
		System.out.println(sum % div);
	}
}
```
