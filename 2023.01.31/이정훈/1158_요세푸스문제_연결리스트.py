class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0

    def __len__(self):
        return self.size
        
    def insert(self,key):
        new_node = Node(key)
        if self.size == 0 :
            self.head = new_node
            self.tail = new_node
            self.tail.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1

    def delete(self, x):
        x.prev.next, x.next.prev = x.next, x.prev
        self.size -= 1

        return x.key

    
    def print_list(self,N,K):
        l = []
        p = self.head.prev
        for _ in range(N):
            for _ in range(K):
                p = p.next
            l.append(self.delete(p))
            
        return l

N,K = map(int, input().split())
linked_list = DoubleLinkedList()

for i in range(1,N+1) :
    linked_list.insert(i)

ans = linked_list.print_list(N,K)
rst = '<'+', '.join(map(str,ans))+'>'
print(rst)