from sys import stdin


num_of_DNAs, length_of_DNAs = map(int, stdin.readline().split())

DNAs = []

min_hamming_distance_DNA = []
min_hamming_distance = 0

for _ in range(num_of_DNAs):
    DNAs.append(stdin.readline())

# 모든 DNA의 각 인덱스를 비교
for nucleotide_idx in range(length_of_DNAs):

    for_count = [0] * 4
    for_comparison = []

    for DNA_idx in range(num_of_DNAs):

        for_comparison.append(DNAs[DNA_idx][nucleotide_idx])

        if DNAs[DNA_idx][nucleotide_idx] == 'A':
            for_count[0] += 1

        elif DNAs[DNA_idx][nucleotide_idx] == 'C':
            for_count[1] += 1

        elif DNAs[DNA_idx][nucleotide_idx] == 'G':
            for_count[2] += 1

        elif DNAs[DNA_idx][nucleotide_idx] == 'T':
            for_count[3] += 1

    if for_count[0] == max(for_count):
        selected_nucleotied = 'A'

    elif for_count[1] == max(for_count):
        selected_nucleotied = 'C'

    elif for_count[2] == max(for_count):
        selected_nucleotied = 'G'

    elif for_count[3] == max(for_count):
        selected_nucleotied = 'T'

    min_hamming_distance_DNA.append(selected_nucleotied)

    # 해당 인덱스에서 선택된 뉴클레오타이드의 수를 빼 문자가 다른 것의 갯수 얻기
    min_hamming_distance += (num_of_DNAs - for_comparison.count(selected_nucleotied))

print(''.join(min_hamming_distance_DNA))
print(min_hamming_distance)
