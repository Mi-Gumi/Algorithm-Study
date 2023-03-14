text1 = list(input()) # 글 1
text2 = list(input()) # 글 2
words = set(text1) & set(text2)
lt1 = len(text1)
lt2 = len(text2)

'''
글자를 탐색을 하여 우선순위에 대한 값을 찾아보기 위해
dp 혹은 탐색(이분탐색)을 진행 하려고 했었음.

0 0 A C A Y K P
0 0 0 0 0 0 0 0
C 0 0 1 1 1 1 1
A 0 1 1 2 2 2 2
P 0 0 0 0 0 0 0
C 0 0 0 0 0 0 0
A 0 0 0 0 0 0 0
K 0 0 0 0 0 0 0
 -> 과 같이 matrix 를 만들어 두고 
 겹치는 값이 있을 대 1 씩 늘려주면 결과 값이 나옴
 Padding을 준 이유는 idx의 편의성 도 있지만, 초기의 값을 설정할 때 
 matrix[-1][-1] 이 되어 이전의 값을 받아오는 일을 방지하기 위해 
 padding을 설정
'''

matrix =[[0 for _ in range(lt1+1)] for _ in range(lt2+1)]
ans = 0
for i in range(1,lt2+1):
  for j in range(1,lt1+1):
    if text2[i-1] == text1[j-1]:        # matrix에 있는 글자가 동일하담ㄴ
      matrix[i][j] = matrix[i-1][j-1]+1 # 1을 추가해준다.

    else:                         
      matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
      # text1 에서 부터 시작해 가져오는 문자열과
      # text2 에서(이전에서 부터 쌓아온) 문자열과
      # 계산되는 문자열의 길이를 비교했을 때 큰값을 가져옴

print(matrix[lt2][lt1])