# [Gold II] 빵집 - 3109 

[문제 링크](https://www.acmicpc.net/problem/3109) 

### 성능 요약

메모리: 49764 KB, 시간: 432 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 그리디 알고리즘

### 문제 설명

<p>유명한 제빵사 김원웅은 빵집을 운영하고 있다. 원웅이의 빵집은 글로벌 재정 위기를 피해가지 못했고, 결국 심각한 재정 위기에 빠졌다.</p>

<p>원웅이는 지출을 줄이고자 여기저기 지출을 살펴보던 중에, 가스비가 제일 크다는 것을 알게되었다. 따라서 원웅이는 근처 빵집의 가스관에 몰래 파이프를 설치해 훔쳐서 사용하기로 했다.</p>

<p>빵집이 있는 곳은 R*C 격자로 표현할 수 있다. 첫째 열은 근처 빵집의 가스관이고, 마지막 열은 원웅이의 빵집이다.</p>

<p>원웅이는 가스관과 빵집을 연결하는 파이프를 설치하려고 한다. 빵집과 가스관 사이에는 건물이 있을 수도 있다. 건물이 있는 경우에는 파이프를 놓을 수 없다.</p>

<p>가스관과 빵집을 연결하는 모든 파이프라인은 첫째 열에서 시작해야 하고, 마지막 열에서 끝나야 한다. 각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결할 수 있고, 각 칸의 중심끼리 연결하는 것이다.</p>

<p>원웅이는 가스를 되도록 많이 훔치려고 한다. 따라서, 가스관과 빵집을 연결하는 파이프라인을 여러 개 설치할 것이다. 이 경로는 겹칠 수 없고, 서로 접할 수도 없다. 즉, 각 칸을 지나는 파이프는 하나이어야 한다.</p>

<p>원웅이 빵집의 모습이 주어졌을 때, 원웅이가 설치할 수 있는 가스관과 빵집을 연결하는 파이프라인의 최대 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 R과 C가 주어진다. (1 ≤ R ≤ 10,000, 5 ≤ C ≤ 500)</p>

<p>다음 R개 줄에는 빵집 근처의 모습이 주어진다. '.'는 빈 칸이고, 'x'는 건물이다. 처음과 마지막 열은 항상 비어있다.</p>

### 출력 

 <p>첫째 줄에 원웅이가 놓을 수 있는 파이프라인의 최대 개수를 출력한다.</p>

---
### Solution
###python
```python
import sys
input = sys.stdin.readline

def dfs(x, y):
    if y == C-1:
        return True
    
    for num in [-1,0,1]:
        nx = x + num
        ny = y + 1

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and arr[nx][ny] != 'x':
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
ans = 0

for i in range(R):
    if dfs(i,0): ans += 1

print(ans)
```

### java
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[][] visited;
	static char[][] arr;
	static int R;
	static int C;
	static int ans;
	static int[] dir = {-1, 0, 1};
	
	static boolean dfs(int x, int y) {
		if (y == C-1) {
			return true;
		}
		
		for (int num : dir) {
			int nx = x + num;
			int ny = y + 1;
			
			if (0 <= nx && nx < R) {
				if (arr[nx][ny] != 'x' && visited[nx][ny] == false) {
					visited[nx][ny] = true;
					if (dfs(nx, ny)) {
						return true;
					}
				}
			}
		}
		return false;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		arr = new char[R][C];
		
		for (int i = 0; i < R; i++) {
			arr[i] = br.readLine().toCharArray();
		}
		
		ans = 0;
		visited = new boolean[R][C];
		for (int i = 0; i < R; i++) {
			if (dfs(i, 0)) ans++;
		}
		System.out.println(ans);
	}
}
```
