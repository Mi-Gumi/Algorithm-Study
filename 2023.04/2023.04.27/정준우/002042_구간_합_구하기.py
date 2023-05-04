from sys import stdin


def make_segment_tree(node, start, end):

    if start == end:
        segment_tree[node] = nums[start]
        return segment_tree[node]

    mid = (start + end) // 2

    child_left = make_segment_tree(node * 2, start, mid)
    child_right = make_segment_tree(node * 2 + 1, mid + 1, end)

    segment_tree[node] = child_left + child_right

    return segment_tree[node]


def segment_tree_sum(node, start, end, entire_start, entire_end):

    if entire_start <= start and end <= entire_end:
        return segment_tree[node]

    elif start > entire_end or end < entire_start:
        return 0

    mid = (start + end) // 2

    sum_left = segment_tree_sum(node * 2, start, mid, entire_start, entire_end)
    sum_right = segment_tree_sum(node * 2 + 1, mid + 1, end, entire_start, entire_end)

    return sum_left + sum_right


def update_segment_tree(node, start, end, idx, diff):

    if idx < start or idx > end:
        return

    segment_tree[node] += diff

    if start != end:
        mid = (start + end) // 2

        update_segment_tree(node * 2, start, mid, idx, diff)
        update_segment_tree(node * 2 + 1, mid + 1, end, idx, diff)


num_of_numbers, num_of_updates, num_of_sums = map(int, stdin.readline().split())

segment_tree = [0 for _ in range(num_of_numbers * 4)]

nums = []
for _ in range(num_of_numbers):
    nums.append(int(stdin.readline()))

make_segment_tree(1, 0, num_of_numbers - 1)

for _ in range(num_of_updates + num_of_sums):
    a, b, c = map(int, stdin.readline().strip().split())

    if a == 1:
        diff = c - nums[b - 1]
        nums[b - 1] = c

        update_segment_tree(1, 0, num_of_numbers - 1, b - 1, diff)

    else:
        print(segment_tree_sum(1, 0, num_of_numbers - 1, b - 1, c - 1))
