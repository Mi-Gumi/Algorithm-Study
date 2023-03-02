# [Gold V] LCS - 9251 

[문제 링크](https://www.acmicpc.net/problem/9251) 

### 성능 요약

메모리: 55712 KB, 시간: 580 ms

### 분류

다이나믹 프로그래밍(dp), 문자열(string)

### 문제 설명

<p>LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.</p>

<p>예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.</p>

### 입력 

 <p>첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.</p>

### 출력 

 <p>첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.</p>
 
 ---
 ### Solution
 ```python
import sys
input = sys.stdin.readline

# strip을 안쓰면 \n 까지 문자로 들어가서 len이 +1 된다.
str1 = input().strip()
str2 = input().strip()

# 0의 자리까지 이용해야하기 때문에 +1 해준다(idx)
str1_len = len(str1)+1
str2_len = len(str2)+1

# 중요... N,M의 길이가 다르기 때문에 row, col 제대로 해줘야한다.
# 문자길이가 달라지게 되면 for문에서 index에러난다...
Lcs_lst = [[0] * str2_len for _ in range(str1_len)]

for i in range(1,str1_len):
    for j in range(1,str2_len):
        # 같을 경우 이전 단어의 이전 비교 값에 +1
        if str1[i-1] == str2[j-1]:
            Lcs_lst[i][j] = Lcs_lst[i-1][j-1] + 1
        # 같지 않으면, 해당 문자를 스킵하거나, 이전 문자열을 스킵
        else:
            Lcs_lst[i][j] = max(Lcs_lst[i][j-1], Lcs_lst[i-1][j])

# 가장 마지막 idx는 가장 많이 겹치는 값을 가진다.
print(Lcs_lst[str1_len-1][str2_len-1])
