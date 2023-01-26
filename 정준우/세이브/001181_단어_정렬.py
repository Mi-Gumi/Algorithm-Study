num = int(input())

word_list = list()

for cycle in range(num):
    word_list.append(input())

# set 를 통해 중복 제거, 사전 순서대로 정렬 후 길이에 따라 정렬
compressed_list = list(set(word_list))
compressed_list.sort()
compressed_list.sort(key = len)


for i in compressed_list:
    print(i)