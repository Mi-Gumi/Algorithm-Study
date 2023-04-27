# [Silver IV] DNA - 1969 

[문제 링크](https://www.acmicpc.net/problem/1969) 

### 성능 요약

메모리: 15164 KB, 시간: 152 ms

### 분류

브루트포스 알고리즘, 그리디 알고리즘, 구현, 문자열

### 문제 설명

<p>DNA란 어떤 유전물질을 구성하는 분자이다. 이 DNA는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다(Adenine, Thymine, Guanine, Cytosine). 우리는 어떤 DNA의 물질을 표현할 때, 이 DNA를 이루는 뉴클레오티드의 첫글자를 따서 표현한다. 만약에 Thymine-Adenine-Adenine-Cytosine-Thymine-Guanine-Cytosine-Cytosine-Guanine-Adenine-Thymine로 이루어진 DNA가 있다고 하면, “TAACTGCCGAT”로 표현할 수 있다. 그리고 Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수이다. 만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.</p>

<p>우리가 할 일은 다음과 같다. N개의 길이 M인 DNA s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>n</sub>가 주어져 있을 때 Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다. 즉, s와 s<sub>1</sub>의 Hamming Distance + s와 s<sub>2</sub>의 Hamming Distance + s와 s<sub>3</sub>의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.</p>

### 입력 

 <p>첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다. N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고, 둘째 줄에는 그 Hamming Distance의 합을 출력하시오. 그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.</p>

---

### Solution
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
    	// 처음 받을 때 문자열 그대로 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 공백을 기준으로 담기
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 담은 토큰들 n, m에 넣어주기
        int N = Integer.parseInt(st.nextToken()); // dna 수
        int M = Integer.parseInt(st.nextToken()); // 문자열의 길이
        String[] s = new String[N];
        for (int i = 0; i < N; i++) {
			s[i] = br.readLine();
		}
        
        int sum = 0;
        String result = "";
        for(int i = 0; i < M; i++) {
			int max = -1;
			int idx = 0;
			int arr[] = new int[4];
			for (int j = 0; j < N; j++) {
				if (s[j].charAt(i) == 'A') {
					arr[0]++;
				} else if (s[j].charAt(i) == 'C') {
					arr[1]++;
				} else if(s[j].charAt(i) == 'G') {
					arr[2]++; 
				} else {
					arr[3]++;
				}
			}
			for (int j = 0; j <4; j++) {
				if (arr[j] > max) {
					max = arr[j];
					idx = j;
				}
			}
			if (idx == 0) {
				result += 'A';
			} else if (idx == 1) {
				result += 'C';
			} else if (idx == 2) {
				result += 'G';
			} else if (idx == 3) {
				result += 'T';
			}
			for (int j = 0; j < 4; j++) {
				if (j != idx) {
					sum += arr[j];
				}
			}
        }
        System.out.println(result);
        System.out.println(sum);
    }
}
