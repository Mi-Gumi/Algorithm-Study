# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이
# 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.


##############################################################################
# 공통 부분만으로 제일 긴 길이를 가진 조합부터 찾다가 결과가 나오면 측시 break  => 메모리 초과


# from itertools import combinations
#
#
# A = list(input())
# B = list(input())
# commonA = []
# for i in range(len(A)) :
#     if A[i] in B :
#         commonA.append(A[i])
# commonB = []
# for i in range(len(B)) :
#     if B[i] in A :
#         commonB.append(B[i])
# L = min(len(commonA), len(commonB))
# _max = 0
# while _max == 0 :
#     comA = list(combinations(commonA, L ))
#     comB = list(combinations(commonB, L))
#     for c in comA :
#         if c in comB :
#             _max = L
#             break
#     L -= 1
#
# print(_max)


############################################################################
#비트 마스킹을 통해 공통 부분문 0과 1로 재귀를 통해 순열 구함 => 메모리초과

# def permutation(n, k, arr, save):  # n : 원소의 갯수, k : 현재 depth
#     if n == k:  # basis
#         tmp = []
#         for i in range(n) :
#             if bit[i] == 1:
#                 tmp.append(arr[i])
#         save.append(tmp)
#
#     else:  # inductive
#         if arr[k] in common :
#             # 포함 될때
#             bit[k] = 1
#             permutation(n, k + 1, arr, save)
#
#             # 포함되지 않을 때
#             bit[k] = 0
#             permutation(n, k + 1, arr, save)
#         else :
#             permutation(n, k + 1, arr, save)
#
#
# A = list(input())
# B = list(input())
#
# A_set = set(A)
# B_set = set(B)
# common = A_set.intersection(B_set)
#
# A_len = len(A)
# B_len = len(B)
# bit = [0] * A_len
# permutA = []
# permutation(A_len,0,A, permutA)
#
# bit = [0] * B_len
# permutB = []
# permutation(B_len,0,B, permutB)
#
# _max = 0
# for p in permutA :
#     if p in permutB and _max < len(p):
#         _max = len(p)
#
# print(_max)
#
#
