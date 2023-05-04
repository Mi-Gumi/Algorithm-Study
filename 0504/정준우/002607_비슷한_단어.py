# Counter 모듈 사용
# iterable 자료 내 요소의 종류를 key, 해당 요소의 수를 value로 가지는 dict 생성
from sys import stdin
from collections import Counter


num_of_words = int(stdin.readline())

main_word = stdin.readline().strip()

main_word_count = Counter(main_word)

yusa_word = 0

for _ in range(num_of_words - 1):

    word_for_check = stdin.readline().strip()

    check_word_count = Counter(word_for_check)

    # 아예 같은 단어
    if main_word_count == check_word_count:
        yusa_word += 1
        continue

    # 단어 길이 차이가 2 이상 난다면 두 문자 이상을 건드려야 하기 때문에 유사 단어 아님
    if abs(len(main_word) - len(word_for_check)) >= 2:
        continue

    # 더 긴 단어의 Counter 결과에서 다른 단어의 Counter 결과를 뺐을 때,
    if len(main_word) >= len(word_for_check):
        diff_count = main_word_count - check_word_count

    elif len(main_word) < len(word_for_check):
        diff_count = check_word_count - main_word_count

    # Counter.most_common([n]) => Counter에서 n개의 가장 흔한 요소와 그 개수를 나열한 리스트를 반환
    # 다른 요소의 종류가 한 가지이며, 그 수가 1개 이하라면 유사 단어
    if len(diff_count) == 1 and diff_count.most_common(1)[0][1] <= 1:
        yusa_word += 1

print(yusa_word)
