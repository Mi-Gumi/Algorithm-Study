text1 = list(input())
text2 = list(input())
words = set(text1) & set(text2)
lt1 = len(text1)
lt2 = len(text2)

matrix =[[0 for _ in range(lt1+1)] for _ in range(lt2+1)]
ans = 0
for i in range(1,lt2+1):
  for j in range(1,lt1+1):
    if text2[i-1] == text1[j-1]:
      matrix[i][j] = matrix[i-1][j-1]+1
    else:
      matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

print(matrix[lt2][lt1])