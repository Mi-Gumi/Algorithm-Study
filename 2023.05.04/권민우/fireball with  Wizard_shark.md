# [Gold IV] 마법사 상어와 파이어볼 - 20056 

[문제 링크](https://www.acmicpc.net/problem/20056) 

### 성능 요약

메모리: 131224 KB, 시간: 312 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p><a href="/problem/19237">어른 상어</a>가 마법사가 되었고, 파이어볼을 배웠다.</p>

<p>마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (r<sub>i</sub>, c<sub>i</sub>), 질량은 m<sub>i</sub>이고, 방향은 d<sub>i</sub>, 속력은 s<sub>i</sub>이다. 위치 (r, c)는 r행 c열을 의미한다.</p>

<p>격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.</p>

<p>파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.</p>

<table class="table table-bordered table-center-10 td-center">
	<tbody>
		<tr>
			<td>7</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>6</td>
			<td> </td>
			<td>2</td>
		</tr>
		<tr>
			<td>5</td>
			<td>4</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.</p>

<ol>
	<li>모든 파이어볼이 자신의 방향 d<sub>i</sub>로 속력 s<sub>i</sub>칸 만큼 이동한다.

	<ul>
		<li>이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.</li>
	</ul>
	</li>
	<li>이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
	<ol>
		<li>같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.</li>
		<li>파이어볼은 4개의 파이어볼로 나누어진다.</li>
		<li>나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
		<ol>
			<li>질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.</li>
			<li>속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.</li>
			<li>합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.</li>
		</ol>
		</li>
		<li>질량이 0인 파이어볼은 소멸되어 없어진다.</li>
	</ol>
	</li>
</ol>

<p>마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.</p>

### 입력 

 <p>첫째 줄에 N, M, K가 주어진다.</p>

<p>둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 r<sub>i</sub>, c<sub>i</sub>, m<sub>i</sub>, s<sub>i</sub>, d<sub>i</sub>로 이루어져 있다.</p>

<p>서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.</p>

### 출력 

 <p>마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.</p>

---

### Solution
```python
import sys
input = sys.stdin.readline

def fireball_move():
    for r, c, m, s, d in fireball_lst:
        nr = (r + (direc[d][0] * s)) % N
        nc = (c + (direc[d][1] * s)) % N

        arr[nr][nc].append([m, s, d])


def fireball_divide():
    global fireball_lst
    fireball_lst = []
    for i in range(N):
        if K == 1 and i == 6:
            pass
        for j in range(N):
            cnt = len(arr[i][j])
            if cnt >= 2:
                odd = 0
                even = 0
                total_m = 0
                total_s = 0
                for mm, ss, dd in arr[i][j]:
                    total_m += mm
                    total_s += ss
                    if dd % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                total_m = total_m // 5
                if total_m == 0:
                    continue
                total_s = total_s // cnt

                if (even > 0 and odd == 0) or (odd > 0 and even == 0):
                    for k in range(0,7,2):
                        fireball_lst.append((i, j, total_m, total_s, k))
                else:
                    for k in range(1,8,2):
                        fireball_lst.append((i, j, total_m, total_s, k))
            elif cnt == 1:
                fireball_lst.append((i, j, arr[i][j][0][0], arr[i][j][0][1], arr[i][j][0][2]))

N, M, K = map(int, input().split())
direc = [(-1, 0), (-1, 1), (0, 1), (1, 1),
         (1, 0), (1, -1), (0, -1), (-1, -1)]

fireball_lst = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball_lst.append((r - 1, c - 1, m, s, d))

while K != 0:
    arr = [[[] for _ in range(N)] for _ in range(N)]
    fireball_move()
    fireball_divide()
    K -= 1

ans = 0
for fireball in fireball_lst:
    ans += fireball[2]

print(ans)
