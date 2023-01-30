import sys
input = sys.stdin.readline

#클래스 원형 연결 리스트 선언
class Circle_Linked_List:
    # 원형 연결 리스트 초기화 함수
    def __init__(self):
        # 첫번째 노드와 마지막 노드를 None으로 설정
        # 리스트 사이즈를 0으로 설정
        self.head = None
        self.tail = None
        self.size = 0
    
    # 원형 연결 리스트 클래스 내부에서 클래스 노드 선언
    class Node:
        # 노드 초기화 함수
        # 입력 받은 데이터를 노드의 데이터로 설정
        # next의 기본값은 None, 노드의 next를 next로 설정
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    # 리스트에 데이터를 추가하는 함수
    def add(self, data):
        # 만약 리스트의 사이즈가 0이라면
        if self.size == 0:
            # 리스트의 첫번째 노드가 입력받은 데이터로 만든 노드가 되도록 설정
            self.head = self.Node(data)
            # 첫번째 노드가 첫번째 노드를 가리키도록 설정
            self.head.next = self.head
            # 마지막 노드를 첫번째 노드로 설정
            self.tail = self.head
            # 리스트 사이즈 + 1
            self.size += 1
            return
        # 리스트의 사이즈가 0이 아니라면
        else:
            # 입력받은 데이터로 노드 생성
            node = self.Node(data)
            # 생성된 노드가 첫번째 노드를 가리키도록 설정
            node.next = self.head
            # 마지막 노드가 생성된 노드를 가리키도록 설정
            self.tail.next = node
            # 마지막 노드를 생성된 노드로 설정
            self.tail = node
            # 리스트 사이즈 + 1
            self.size += 1
            return
    
    # 리스트 내부의 노드의 데이터를 모두 출력하는 함수
    def print_list(self):
        # 현재 노드를 첫번째 노드로 설정
        current_node = self.head
        # 현재 노드의 다음이 첫번째 노드가 아니라면
        while current_node.next is not self.head:
            # 현재 노드 출력
            print(current_node.data)
            # 현재 노드는 현재 노드의 다음 노드로 설정
            current_node = current_node.next
        # 마지막 노드에서 반복문이 실행되지 않고 멈추기 때문에 현재 노드 출력
        print(current_node.data)
        return

    # 리스트의 마지막 노드에서 K만큼 이동한 노드를 찾아주는 함수
    def find_next(self, K):
        # 마지막 노드를 마지막 노드에서 K만큼 이동한 노드로 설정
        for _ in range(K):
            self.tail = self.tail.next
        return
    
    # 마지막 노드의 다음 노드를 제거하고 마지막 노드의 다음 노드의 데이터를 반환하는 함수
    def remove_next(self):
        # 만약 리스트의 사이즈가 1이라면
        if self.size == 1:
            # 마지막 노드의 다음 노드를 삭제할 노드에 저장
            rm_node = self.tail.next
            # 리스트의 첫번째 노드를 None으로 설정
            self.head = None
            # 리스트의 마지막 노드를 None으로 설정
            self.tail = None
            # 리스트 사이즈 -1
            self.size -= 1
            # 삭제할 노드의 데이터 반환
            return rm_node.data
        else:
            # 마지막 노드의 다음 노드를 삭제할 노드에 저장
            rm_node = self.tail.next
            # 마지막 노드가 삭제할 노드가 가리키던 노드를 가리키도록 설정
            self.tail.next = rm_node.next
            # 리스트 사이즈 -1
            self.size -= 1
            # 삭제할 노드의 데이터 반환
            return rm_node.data

# 요세푸스 순열을 만드는 함수
def Josephus(CLlist, N, K):
    # 정답 배열 선언
    ans = []

    for _ in range(N):
        # K - 1 만큼 이동
        CLlist.find_next(K - 1)
        # K - 1 만큼 이동한 노드의 다음 노드를 삭제하고 ans에 삭제한 노드의 데이터 추가
        ans.append(CLlist.remove_next())
    # 정답 배열 반환
    return ans

N, K = map(int, input().split())

# 원형 연결 리스트 생성
CLlist = Circle_Linked_List()

# 1 부터 N 까지 원형 연결 리스트에 추가
for i in range(1, N + 1):
    CLlist.add(i)

# 정답 배열 생성
ans = Josephus(CLlist, N, K)

# 정답 배열 출력
print('<', end = '')
for i in range(len(ans) - 1):
    print(ans[i], end = ', ')
print(f'{ans[-1]}>')
