import sys
from collections import deque

# 전체 인원과 몇 번째마다 제거되는지 변수로 지정
num_of_potatos, gamzajeon = map(int, sys.stdin.readline().split())

# 인원수만큼의 크기를 가지며, 숫자가 차례대로 들어간 round_table 큐 생성
# 1부터 시작되어야 하니 range 범위 조정
round_table = deque(potato for potato in range(1, num_of_potatos + 1))

# 제거된 인원의 숫자를 차례대로 넣을 빈 리스트 생성
answer_list = []

# 모든 인원이 제거되어 round_table 큐의 길이가 0이 될때까지 반복
while len(round_table) != 0:
    # 만약 세번째 인원을 제거한다면, 2번 왼쪽으로 회전시켰을 때 해당 인원이 큐의 제일 왼쪽에 위치한다
    round_table.rotate(-(gamzajeon - 1))
    # round_table 큐에서 제일 왼쪽 요소를 빼 answer_list에 추가
    answer_list.append(round_table.popleft())

# 완성된 리스트에서 [ ]를 빼고 요소 사이에 ,  를 넣기 위해 join 메서드 사용
print(f'<{", ".join(map(str, answer_list))}>')






'''
# 노드 클래스 지정
class Node:
    def __init__(self, element):
        # 노드에 저장되는 요소 지정
        self.element = element
        # 다음 노드의 주소를 저장 - 막 만들어졌으니 지금은 None
        self.next = None


# 연결 리스트 클래스 지정
class LinkedList:
    def __init__(self):
        # 헤드 노드 지정
        self.head = None
        # 노드의 개수가 탐색에 필요하므로, 이를 저장할 size 변수
        self.size = 0

    # 연결리스트의 크기
    def __len__(self):
        return self.size

    # 앞에 노드를 추가
    def pushFront(self, element):
        # 새 노드 추가
        new_node = Node(element)
        # 새 노드의 다음 값을 헤드 노드로 연결
        new_node.next = self.head
        # 새 노드를 헤드 노드로 선언
        self.head = new_node
        self.size += 1
        return True

    # 뒤에 노드를 추가
    def pushBack(self, element):
        # 새 노드 추가
        new_node = Node(element)
        # 빈 연결리스트일때, 새 노드가 곧 헤드
        if self.size == 0:
            self.head = new_node
        # 빈 연결리스트가 아닐때
        else:
            back = self.head
            # 연결리스트의 끝까지 갈때까지 tail 선언 반복
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self_size += 1

    def popFront(self):
        # 빈 리스트가 아닐 때
        if self.size > 0:
            element = self.head.element
            # 제일 앞의 것을 빼기 때문에 헤드 노드가 다음 노드로 변경
            self.head = self.head.next
            self.size -= 1
            return element
        # 빈 리스트일 때
        return None

    def popBack(self):
        # 빈 리스트가 아닐 때
        if self.size > 0:
            prev, back = None, self.head
            # 연결 리스트의 제일 끝까지 갈 때까지
            while back.next != None:
                prev, back = back, back.next
            element = back.element
            # 노드가 하나뿐이라면
            if self.head == back:
                self.head = None
            else:
                prev.next = back.next
            self_size -= 1
            return key
        else:
            return None

    def search(self, element):
        # 헤드 노드에서 시작
        x = self.head
        # x가 None이 아니라면, 현재 노드의 값이 입력받은 값과 같은지 계속 반복하며 탐색
        while x:
            if x.element == element:
                # 발견하면 x 반환, 아니라면 다음 노드로 이동
                return x
            x = x.next
        # 찾지 못하고 x.next가 None, 즉 연결리스트가 끝나버리면 None 인 x 반환
        return x

    def remove(self, x):
        # 연결리스트가 비어있거나 입력한 요소가 없다면,
        if self.size == 0 or x == None:
            return False
        # 지정한 요소가 제일 앞에 있다면,
        elif x == self.head:
            self.popFront()
            return True
        else:
            prev = self.head
            # 지정한 요소 찾을때까지 반복
            while prev.next != x:
                prev = prev.next
            prev.next = x.next
            self.size -= 1
            return True

N, M = map(int, input().split())
the_list = LinkedList()

# 연결리스트에 인원 추가
for i in range(N, 0, -1):
    the_list.pushFront(i)

# 출력 결과를 담을 빈 리스트 생성
line = []

# 헤드 노드 지정
x = the_list.head

# 몇 번째 인원을 세고 있는지 체크하기 위한 변수 count
count = 0

# 모든 인원이 제외될때까지
while the_list.size != 0:

    # M 동안, count에 1씩 더해가며 노드 이동
    # count가 M과 같아지면, 반복 중단하고 해당 요소 제거 후 리스트에 추가
    # 리스트의 끝까지 가서 포인터가 None이면, 다시 헤드로 향하게 해 순환
    # 위 과정 반복해 연결리스트의 길이가 0이 되면 중단 후 정답 리스트 형식에 맞게 출력
    for _ in range(M):
        if the_list.size == 0:
            break
        count += 1
        if count == M:
            continue
        x = x.next
        if x == None:
            x = the_list.head
    the_list.remove(x)
    line.append(x.element)
    if len(the_list) == 0:
        break
    
print(f'<{", ".join(map(str, line))}>')
'''