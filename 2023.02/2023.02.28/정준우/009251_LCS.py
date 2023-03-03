word1 = input()
word2 = input()

# LCS 알고리즘 표
LCS_matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):

        # 문자가 같으면 해당 문자 직전의 최대값에 + 1
        if word1[i - 1] == word2[j - 1]:
            LCS_matrix[i][j] = LCS_matrix[i - 1][j - 1] + 1

        # 문자가 다르면 직전 값들 중 더 큰 것
        else:
            LCS_matrix[i][j] = max(LCS_matrix[i - 1][j], LCS_matrix[i][j - 1])

print(LCS_matrix[-1][-1])
