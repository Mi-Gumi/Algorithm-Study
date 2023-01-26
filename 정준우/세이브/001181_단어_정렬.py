num = int(input())

word_list = list()

for cycle in range(num):
    word_list.append(input())

compressed_list = list(set(word_list))
compressed_list.sort(key = lambda x: len(x))

test_dict = {len(compressed_list[x]): compressed_list[x] for x in range(len(compressed_list))}

print(compressed_list)
print(test_dict)