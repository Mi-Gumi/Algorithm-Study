from sys import stdin


def recommend(k, v):

    recommended = [False] * (videos + 1)
    checklist = [[v, 1000000001]]

    # 연결되어있는 동영상 중 기준 유사도보다 큰 것의 수 세어주고, 첫 동영상은 제외해야 하니 결과에서 -1
    while checklist:
        video_no, usado = checklist.pop()

        if not recommended[video_no] and usado >= k:
            recommended[video_no] = True
            checklist.extend(video_list[video_no])

    recommends = recommended.count(True)

    return recommends - 1


videos, questions = map(int, stdin.readline().split())

video_list = {i:[] for i in range(videos + 1)}

for _ in range(videos - 1):
    vi, deo, temp_usado = map(int, stdin.readline().split())

    video_list[vi].append([deo, temp_usado])
    video_list[deo].append([vi, temp_usado])

for _ in range(questions):
    selected_usado, current_video = map(int, stdin.readline().split())
    print(recommend(selected_usado, current_video))
